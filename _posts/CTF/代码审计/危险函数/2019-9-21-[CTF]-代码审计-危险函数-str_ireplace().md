str_ireplace

该函数只过滤一次。可被双写绕过。

str_ireplace — str_replace() 的忽略大小写版本

说明

mixed str_ireplace ( mixed $search , mixed $replace , mixed $subject [, int &$count ] )

该函数返回一个字符串或者数组。该字符串或数组是将 subject 中全部的 search 都被 replace 替换（忽略大小写）之后的结果。如果没有一些特殊的替换规则，你应该使用该函数替换带有 i 修正符的 preg_replace() 函数。
