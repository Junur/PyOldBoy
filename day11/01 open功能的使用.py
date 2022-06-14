# @File      : open_func
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/9 2:02 PM
# @Info      :

"""
open() 功能的使用
1. 模式介绍
 控制文件读写内容的模式
  t -- 文本
  b -- 二进制

 控制文件读写操作的模式
  r -- 只读
  w -- 只写
  a -- 只追加写
  + ( r+ 、 w+ 、 a+ )-- 在原有的基础上增加

2. 基本操作流程
    打开文件
    读 / 写文件
    关闭文件

3. 资源回收与 with 语法

4. 详细介绍文件模式 t b r w a +

5. 文件操作的其他方法

6. 文件的高级操作：控制文件指针的移动


1、什么是文件？
    文件是操作系统提供给用户 / 应用程序操作硬盘的一种接口。

    用户/应用程序（open()）
    操作系统（文件）
    计算机硬件（硬盘）

2、为何要用文件？
    用户或应用程序可以通过文件，将数据永久保存到硬盘中。操作文件也就是操作硬盘。

    用户或应用程序直接操作的是文件，对文件进行的所有操作，都是在向操作系统发送系统调用，
    然后再由操作系统将其转换成具体的硬盘操作

3、如何用文件: open()
    控制文件读写内容的模式：t 和 b
        强调 ：t 和 b 不能单独使用，必须和 r / w / a 连用

        t 文本（默认的模式）
            1、读写都是以 str（ unicode ） 为单位的
            2、文本文件
            3、必须指定 encoding = 'utf-8'

        b 二进制 bytes


"""

