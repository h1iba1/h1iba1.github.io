# gmpy2

# 1.pip查看系统有没有安装gmpy2

```javascript
pip search gmpy2
```



# 2.gmpy2的基本概念

gmpy2是一个大数处理的类库，包含了mpz，mpq，mpfr,mpc四种类型

## 2.1 mpz类型

### 介绍：

mpz类型与python内置的int/long类型兼容，但是对于较大的值来说要快得多，提供了各种附加的整数函数

### 使用实列：

```javascript
form gmpy2 import mpz
print(mpz(123456789)*987654321)
#121908186668413269
```



## 2.2 mqp类型

### 介绍：

相当于实际python中的分数

### 实列演示：

```javascript
form gmpy2 import mpq
print(mpq(3,7)/7)
#3/49
```



## 2.3 mpfr类型

Gmpy2中最重要的新特性是支持基于 MPFR 和 MPC 库的正确舍入任意精度的实数和复数算法。 浮点上下文用于控制异常情况。 例如，除以零可以返回 Infinity 或引发异常。

## 2.4mpc



## 3.gmpy2的基本用法

### 3.1 初始化一个大数

```javascript
form gmpy2 import mpz
mpz(9876541236655985555)
```



### 3.2 初始化一个分数

```javascript
form gmpy2 import mpq
mpq(3)/7
```



### 3.3 取模运算

```javascript
pow(mpz(99),37,59)
```



### 3.4 开平方

```javascript
gmpy2.isqrt(81)
```



### 3.5 求最大公因数

```javascript
gmpy2.gcd(495,378)
```



### 3.6 求最大公倍数

```javascript
gmpy2.lcm(5,7)
```



### 3.7 求逆元

```javascript
gmpy2.invert(e,fie_n)

在rsa中已知e和fie_n时，使用该函数可直接求出d
```

