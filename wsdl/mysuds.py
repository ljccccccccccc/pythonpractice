import requests
import html
import os


url = "http://172.16.80.14:8060/services/WorkflowService"

payload="<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:web=\"webservices.services.weaver.com.cn\">\r\n    <soapenv:Header/>\r\n    <soapenv:Body>\r\n        <web:getToDoWorkflowRequestList>\r\n            <web:in0>1</web:in0>\r\n            <web:in1>10</web:in1>\r\n            <web:in2>100</web:in2>\r\n            <web:in3>1453</web:in3>\r\n            <web:in4>\r\n                <!--Zero or more repetitions:-->\r\n                <web:string></web:string>\r\n            </web:in4>\r\n        </web:getToDoWorkflowRequestList>\r\n    </soapenv:Body>\r\n</soapenv:Envelope>"
headers = {
  'Content-Type': 'application/xml',
  'Cookie': 'ecology_JSessionId=abcnA5nv-f_o17oN5YrFx'
}

response = requests.request("POST", url, headers=headers, data=payload)

res = html.unescape(response.text)
myxml = res.encode(encoding='utf-8').decode(encoding='utf-8')
print(myxml)

# 创建文件
f = open('ecology.xml','w+')
f.truncate()
print(myxml)
f.write(myxml)
f.close()
print('over...')
