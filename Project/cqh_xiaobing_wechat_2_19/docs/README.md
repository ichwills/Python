# xiaobing-chat 

![python](https://img.shields.io/badge/python-2.7-red.svg) ![python3.5](https://img.shields.io/badge/python-3.5-blue.svg)     **[中文版](/README.md)**

**xiaobing-chat** is an open source WeChat robot based on  [littlecodersh](https://github.com/littlecodersh)'s [ItChat](https://github.com/littlecodersh/ItChat) project

## Quick Start
1. Download/Clone all the files

```bash
git clone https://gitee.com/icq_belief/cqh_xiaobing_wechat_2_19.git
```

1. Install Python and dependent packages:

    - requests

        ```shell
        pip install requests
        ```
    
    - ItChat

        ```bash
        pip install itchat
        ```


1. execute wechat.py


## Responsed Message Type
### Private Message
| Message Type | Responsed | Way | Output | 
| --- | --- | --- | --- | 
| Text(emoji) | √ | xiaobing response | message details | 
| Map | o | xiaobing response | message details | 
| Card | √ | static text | message details | 
| Note | × | - | - | 
| Sharing | √ | xiaobing response | message details | 
| Picture | √ | download & send img | storage path | 
| Recoring | √ | download & send img | storage path | 
| Attachments | √ | download & static text | storage path | 
| Video | o | download & send img | storage path | 
| Friend | √ | add friend & welcome message | - | 

### Group chat
| Message Type | @me | Responsed | Way | Output | 
| --- | --- | --- | --- | --- | 
| Text(emoji) | yes | √ | xiaobing response | message details | 
| Text(emoji) | no | × | - | message details | 
| Picture | - | √ | send img | storage path | 
| Others | - | × | - | - | 


## TODO
 - Enhance compatibility
 - Improve and add new message types

## Experimental Feature
Try to recongnize friends' recording messages with Baidu's REST API. To enable the feature, [ffmpeg](http://ffmpeg.org/) and [pydub](https://github.com/jiaaro/pydub) package is required, and you have to set the value of enable_voice_rec to True in wechat.py file.

## Issues and Suggestions
Any issues and suggestions may be discussed.

## License
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
