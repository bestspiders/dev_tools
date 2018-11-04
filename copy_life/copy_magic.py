#-*- coding:utf-8 -*-
import sys,socket,json,os,shutil,base64,urllib2,urllib

def get_host_ip():
    try:
        sock_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock_conn.connect(('8.8.8.8', 80))
        ip = sock_conn.getsockname()[0]
    finally:
        sock_conn.close()

    return ip
def send_task_status(post_url,status,task_id):
    status_data={'status':status,'task_id':task_id}
    result_req=urllib2.Request(url=post_url,data=urllib.urlencode(status_data))
    response=urllib2.urlopen(result_req)
    print response.read()

if __name__ == '__main__':
    post_data={'tag_name':"test_host",'host':get_host_ip()}
    copy_main_url="http://0.0.0.0/copy_life/copy_copy_copy.php"#修改为你的ip
    post_url='http://0.0.0.0/copy_life/change_status.php'#修改为你的ip
    proxy_ip=''#有则填写
    if proxy_ip:
        proxy_support = urllib2.ProxyHandler({"http":proxy_ip,'https':proxy_ip})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
    req=urllib2.Request(url=copy_main_url,data=urllib.urlencode(post_data))
    res=urllib2.urlopen(req)
    res_content=res.read()
    path_dic=json.loads(res_content)
    if not path_dic['src']:
        print u"没有可以复制的"
        sys.exit()
    path_dic['src']=base64.b64decode(path_dic['src'])
    path_dic['dest']=base64.b64decode(path_dic['dest'])
    if os.path.exists(path_dic['src']):
        print path_dic
        if os.path.isdir(path_dic['src']):
            if not os.path.exists(path_dic['dest']):#是文件夹并且不存在,则创建
                os.makedirs(path_dic['dest'])
                send_task_status(post_url=post_url,status=2,task_id=path_dic['task_id'])
        else:
            file_name=os.path.basename(path_dic['dest'])
            list_path=os.path.dirname(path_dic['dest'])
            src_file_size=os.path.getsize(path_dic['src'])
            if not os.path.exists(list_path):#文件目录不存在则创建
                os.makedirs(list_path)
            if not os.path.exists(path_dic['dest']):#文件不存在则复制
                shutil.copyfile(path_dic['src'],path_dic['dest'])
                send_task_status(post_url=post_url,status=2,task_id=path_dic['task_id'])
            elif src_file_size!=os.path.getsize(path_dic['dest']):#文件大小不一致则复制
                shutil.copyfile(path_dic['src'],path_dic['dest'])
                send_task_status(post_url=post_url,status=2,task_id=path_dic['task_id'])
    else:
        send_task_status(post_url=post_url,status=3,task_id=path_dic['task_id'])
