<!--
 * @Author: 七画一只妖 1157529280@qq.com
 * @Date: 2023-03-27 09:43:36
 * @LastEditors: 七画一只妖 1157529280@qq.com
 * @LastEditTime: 2023-03-27 14:55:12
 * @FilePath: \060坎公骑冠剑会战工具\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# BaseKnightReport
## 坎公会战工具（更新中）

### 使用方法
1.在payload目录下新建文件cookies.py并添加以下内容
~~~py
header = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
    "connection": "keep-alive",
    "cookie": "你的cookies",
}
~~~

2.如何获取cookies？
>- 1.浏览器开启无痕模式
>- 2.打开百宝袋地址 https://www.bigfun.cn/tools/gt/
>- 3.在百宝袋页面按下【F12 没有F12右键审元素】打开DEV开发者工具 控制台(Console)输入下面这串代码 复制弹窗文字 粘贴到session-api输入框中提交
~~~js
var strCookie = document.cookie; var arrCookie = strCookie.split("; "); for(var i = 0; i < arrCookie.length; i++){ var arr = arrCookie[i].split("="); if(arr[0] == 'session-api'){alert(arr[1]);} }
~~~
>- 4.关闭无痕窗口浏览器（不要使用bigfun退出登录 会导致接口失效 也不要切换账号会立刻失效）


### 已完成
>- 1.输出每日伤害报表