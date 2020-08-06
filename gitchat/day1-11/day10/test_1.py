import  os
from _collections import defaultdict
import re
# 1、文件的读操作
file_path= '/gitchat/day1-11/day10'
file_name= 'test.txt'
def read_file(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError("%s is not exist"%filename)
    with open(filename,encoding='utf-8') as f:
        content=f.read()
    return content

content=read_file("/gitchat/day1-11/day10/test.txt")
print(content)
# 2、文件按行读（read、readlines每次读取整个文件，readline每次读取一行）
def get_words_count(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError("%s is not exist"%filename)
    rec=re.compile('\s+') #\s 匹配空白字符
    dd=defaultdict(int)
    with open(filename,"r+",encoding='utf-8') as f:
        for line in f:
            clean_line=line.strip()
            if clean_line:
                words=rec.split(clean_line)
                for word in words:
                    dd[word]+=1
    dd=sorted(dd.items(),key=lambda x:x[1],reverse=True)
    return dd
dd=get_words_count(os.path.join(file_path,file_name))
print(dd)
# 3、文件写操作，先判断路径是否存在，不存在，mkdir再写
def write_to_file(file_path,file_name):
    if os.path.exists(file_path) is False:
        os.mkdir(file_path)
    whole_path_filename=os.path.join(file_path,file_name)
    to_write_content = ''' 
                           Hey, Python
                           I just love Python so much,
                           and want to get the whole python stack by this 60-days column
                           and believe!
                           '''
    with open(whole_path_filename,'w',encoding='utf-8') as f_w:
        f_w.write(to_write_content)

    with open(whole_path_filename,'r',encoding='utf-8') as f_r:
        content=f_r.read()
        print(content)
        if to_write_content == content:
            print('content is equal by reading and writing')
        else:
            print('----Warning: NO Equal-----------------')

write_to_file(file_path, "test_2.txt")

# 4、获取文件名，有时拿到一个文件名时，名字带有路径。这时，使用 os.path、split 方法实现路径和文件的分离。
def get_file_name(filename):
     file_ext=os.path.split(filename)
     ipath,ifile=file_ext
     return ipath,ifile

ipath,ifile=get_file_name(os.path.join(file_path,file_name))
print(ipath)
print(ifile)
#5、获取后缀名，os.path 模块，splitext 能够优雅地提取文件后缀。
def get_suffix_name(filename):
    file_extension=os.path.splitext(filename)
    return file_extension[0],file_extension[1]

file_extension_pre,file_extension_suffix=get_suffix_name(os.path.join(file_path,file_name))
print(file_extension_pre)
print(file_extension_suffix)
#6、获取指定后缀名的文件
def get_filenames_with_suffix(file_path,suffix):
    lst=[]
    for filename in os.listdir(file_path):
        splits=os.path.splitext(filename)
        if suffix == splits[1]:
            lst.append(filename)
    return lst
r=get_filenames_with_suffix(file_path,'.py')
print(r)
# 7、批量修改后缀，本案例使用 Python os 模块和 argparse 模块。将工作目录 work_dir 下所有后缀名为 old_ext 的文件，修改为 new_ext
import argparse
def get_parser():
    parser=argparse.ArgumentParser(description='工作目录中文件后缀名修改')
    parser.add_argument('work_dir',metavar='WORK_DIR',type=str,nargs=1,help='修改后缀名的文件目录')
    parser.add_argument('old_ext',metavar='OLD_EXT',type=str,nargs=1,help='原来的后缀')
    parser.add_argument('new_ext',metavar='NEW_EXT',type=str,nargs=1,help='新的后缀')
    return parser
def batch_rename(work_dir,old_ext,new_ext):
    for filename in os.listdir(work_dir):
        split_file=os.path.splitext(filename)
        file_ext=split_file[1]
        if old_ext==file_ext:
            newfile=split_file[0]+new_ext
            os.rename(os.path.join(work_dir,filename),os.path.join(work_dir,newfile))
    print("完成重命名")
    print(os.listdir(work_dir))
# 8、批量获取文件修改时间，os.path.getmtime 返回文件的最后一次修改时间
from datetime import  datetime
print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
def get_modify_time(indir):
    for root,_,files in os.walk(indir):
        for file in files:
            whole_file_name=os.path.join(root,file)
            modify_time=os.path.getatime(whole_file_name)
            nice_show_time=datetime.fromtimestamp(modify_time)
            print('文件 %s 最后一次修改时间：%s' % (file, nice_show_time))
get_modify_time(file_path)
#9、批量压缩文件
import zipfile
import time
def batch_zip(start_dir):
    start_dir=start_dir#路径
    file_news=start_dir+'.zip'#压缩后文件夹的名字
    z=zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        # 这一句很重要，不 replace 的话，就从根目录开始复制
        f_path = dir_path.replace(start_dir, '')
        f_path = f_path and f_path + os.sep  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_news
str_1="123" and "456"
print(str_1)
import hashlib
# 10、32 位文件加密，hashlib 模块支持多种文件的加密策略
def hash_cry32(s):
    m=hashlib.md5()
    m.update((str(s).encode('utf-8')))
    return m.hexdigest()
print(hash_cry32(1))  # c4ca4238a0b923820dcc509a6f75849b
print(hash_cry32('hello'))  # 5d41402abc4b2a76b9719d911017c592

#11、定制文件不同行
def stat_line_cnt(statfile):
    print('文件名：'+statfile)
    cnt=0
    with open(statfile,encoding='utf-8') as f:
        while f.readline():
            cnt+=1
        return cnt

def diff(more,cnt,less):
    difflist=[]
    with open(less,encoding='utf-8') as l:
        with open(more,encoding='utf-8') as m:
            lines=l.readlines()
            for i,line in enumerate(lines):
                if line.strip() != m.readline().strip():
                    difflist.append(i)
    if cnt -i >1:
        difflist.extend(range(i+1,cnt))
    return [no+1 for no in difflist]

def file_diff_line_nos(fileA,fileB):
    try:
        cntA=stat_line_cnt(fileA)
        cntB=stat_line_cnt(fileB)
        if cntA> cntB:
            return diff(fileA,cntA,fileB)
        return diff(fileB,cntB,fileA)
    except Exception as e:
        print(e)
