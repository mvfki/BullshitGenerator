## mvfki Version Update

**1.** Though it is 草 to use Chinese variables but it really sucks :D  
**2.** Modulized as a standard Python module/package. This is just a practice of writing a module/package. Please **DO NOT** use this tool in any formal scenario.  
**3.** Installation:  
- Recommended:
```{bash}
pip install BSG
```
- From source code:
```{bash}
git clone https://github.com/mvfki/BullshitGenerator.git
cd BullshitGenerator
python setup.py install
```
**4.** You got two approach to use it.  
- As a console command line tool:  
```
BSG --help
```
- As a Python importable module:  
```
$ python
>>> import BSG
>>> bs = BSG.bullShit('THEME')
>>> print(bs)
```
See `help(BSG.bullShit)` for more information.  
**5.** Future plan:
- Extend other data files which are like 大草原.
- Implement subcommand that generates the JSON (or maybe other type of formats) data file, so that user can generate their customized bullShit with their favorite words. 

## New feature

Added `bullShit.unlimitedPOOPOO()` method. **BE CAREFUL** when trying it.

## Original copy of this README.md
-----------------------------------------------------------  

# [狗屁不通文章生成器](https://github.com/menzi11/BullshitGenerator)
# [BullshitGenerator](https://github.com/menzi11/BullshitGenerator)

偶尔需要一些中文文字用于GUI开发时测试文本渲染. __本项目只做这一项, 请勿用于其他任何用途__.
Needs to generate some texts to test if my GUI rendering codes good or not. so I made this.

## 再次声明一下, 本项目生成的文章真的狗屁不通, 只能拿来搞笑, 请不要用于正规用途!
## 再次声明一下, 本项目生成的文章真的狗屁不通, 只能拿来搞笑, 请不要用于正规用途!
## 再次声明一下, 本项目生成的文章真的狗屁不通, 只能拿来搞笑, 请不要用于正规用途!

本项目为python3版本, 还有由suulnnka修改在线版, 使用更加方便:
https://suulnnka.github.io/BullshitGenerator/index.html

下一步计划:
1. 防止文章过于内容重复
1. 加入更多啰嗦话.
1. 加入马三立<开会迷>里的内容
1. 加入手写体直接渲染出图片的功能(__仅仅用于测试本人的打印机是否工作正常, 请勿做它用__).

----

## 关于Pull requests:

鄙人每个requests都会仔细阅读, 但因近期事情较多, merge未必及时, 毕竟是业余项目, 请大家见谅. 如果未来实在更新不及时, 也欢迎有志之士替代本人继续本项目.

## 关于中文变量名:

平时撸码鄙人是不写中文变量名的, 本项目中的中文变量名只是最开始瞎写的时候边写语料边写代码时懒得切英文输入法了. 不过既然如此就保持吧!

## 关于生成算法

鄙人才疏学浅并不会任何自然语言处理相关算法. 而且目前比较偏爱简单有效的方式达到目的方式. 除非撞到了天花板, 否则暂时不会引入任何神经网络等算法. 不过欢迎任何人另开分支实现更复杂, 效果更好的算法. 不过除非效果拔群, 否则鄙人暂时不会融合.

