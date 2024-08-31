import streamlit as st
import pandas as pd
import json
import streamlit as st
import os
import zipfile
import time
import shutil

mul_sel = st.sidebar.selectbox(options=['景点图片重命名','json转csv'],label= '选择工具')
if mul_sel == 'json转csv':
    st.title("JSON to csv Converter")

    # 文本输入框
    json_data = st.text_area("请输入 JSON 数据：")
    excel = st.radio(options= ['是','否'],label= '上传excel匹配顺序',index = 1,key=11)
    if excel == '是':
        d1 = st.file_uploader(label = '上传csv')
        if d1 is not None:
            df_excel = pd.read_csv(d1)
            col = st.selectbox(options=df_excel.columns,label='选择匹配列',index=0)

    if json_data:
        try:
            data_dict = json.loads(json_data)
            #df = pd.DataFrame.from_dict(data_dict, orient='index').reset_index()
            df = pd.DataFrame([(key, value) for key, value in data_dict.items()], columns=['景点名', 'json结果'])
            df.columns = ['景点名称', 'json结果']
            types = st.selectbox(options=['是','否'],label= 'list是否合并',index = 1,key = 200)
            if types == '是':
                split_str = st.text_input(label='输入分割符')
                df['json结果']  = df['json结果'].apply(lambda x : split_str.join(x))
            
            if excel == '是':
                df = pd.merge(left=df_excel[[col]],right=df,how='left',left_on=col,right_on='景点名称')
        
            st.download_button(
                label="下载为 csv 文件",
                data=df.to_csv(index=False),
                file_name='景点解析.csv',
            )
                
        except json.JSONDecodeError:
            st.error("输入的 JSON 数据格式不正确。")
            
if mul_sel == '景点图片重命名':
    uploaded_files = st.file_uploader("批量上传文件", accept_multiple_files=True)
    df = ['北京环球度假区',
 '故宫博物院',
 '八达岭长城',
 '中国国家博物馆',
 '颐和园',
 '恭王府',
 '天坛',
 '圆明园',
 '慕田峪长城',
 '北京动物园',
 '天安门广场',
 '北京野生动物园',
 '中国科学技术馆',
 '奥林匹克公园',
 '雍和宫',
 '鸟巢(国家体育场)',
 '什刹海',
 '明十三陵',
 '景山公园',
 '国家自然博物馆',
 '古北水镇',
 '中国地质博物馆',
 '北京欢乐谷',
 '北京海洋馆',
 '北京天文馆',
 '国家大剧院',
 '北海公园',
 '香山公园',
 '南锣鼓巷',
 '水立方(国家游泳中心)',
 '居庸关长城',
 '朝阳公园',
 '泡泡玛特城市乐园',
 '北京大观园',
 '北京汽车博物馆',
 '世界公园',
 '前门大街',
 '王府井',
 '北京杜莎夫人蜡像馆',
 '老舍茶馆',
 '南山滑雪场',
 '孔庙和国子监博物馆',
 '清华大学艺术博物馆',
 '太平洋海底世界',
 '中央广播电视塔',
 '798 艺术区',
 '雁栖湖',
 '大栅栏',
 '北京宋庆龄故居',
 '龙庆峡',
 '潭柘寺',
 '北京欢乐水魔方',
 '德云社剧场',
 '红螺寺',
 '鼓楼',
 '八大处公园',
 '北京奥林匹克塔',
 '中华民族博物院',
 '三里屯',
 '司马台长城',
 '石景山游乐园',
 '首都博物馆',
 '国家图书馆',
 '中国美术馆',
 '北京刘老根大舞台',
 '后海',
 '纪晓岚故居',
 '地坛',
 '人民大会堂',
 '中山公园',
 '玉渊潭公园',
 '红砖美术馆',
 '白云观',
 '亮马河国际风情水岸',
 '北京市档案馆',
 '世贸天阶',
 '西单商业街',
 '中国电影博物馆',
 '中国航空博物馆',
 '青龙峡风景区',
 '国家植物园',
 '陶然亭公园',
 '白塔寺',
 '大运河博物馆',
 '东交民巷',
 '北京平谷金海湖',
 '周口店北京人遗址博物馆',
 '牛街',
 '朝阳剧场',
 '北京西山国家森林公园',
 '玉渡山景区',
 'SOLANA 蓝色港湾',
 '和平菓局',
 '十渡风景名胜区',
 '北京大学-校史馆',
 '黑龙潭风景区',
 '央视总部大楼',
 '白瀑寺',
 '雪都滑雪场',
 '清凉谷风景区',
 '北京西山滑雪场',
 '北京园博园',
 '八大胡同',
 '望京 SOHO',
 '北京温榆河公园',
 '京东大溶洞',
 '北京梨园剧场',
 '日坛公园',
 '华熙 Live·五棵松',
 '五道口',
 '京东大峡谷',
 '京杭大运河',
 '月坛公园',
 '梅兰芳纪念馆',
 '北京工人体育场',
 '张裕爱斐堡酒庄',
 '元大都城垣遗址公园',
 '鬼笑石',
 '海坨山',
 '齐白石旧居纪念馆',
 '梅兰芳大剧院',
 '北京潘家园古玩城',
 '灵境胡同']

    site_name = st.selectbox(options=df,label = '选择景点' )
    types = st.selectbox(options=['打卡机位','打卡姿势'],label = '打卡类型' )

    if uploaded_files:
        st.write(len(uploaded_files))
        target_directory = './renamed_files/'
        if os.path.exists(target_directory):
            try:
                shutil.rmtree(target_directory)
            except PermissionError:
                st.error(f"没有权限删除目录 {target_directory}。")
            except OSError as e:
                st.error(f"删除目录时出现错误：{e}")
        os.makedirs(target_directory)

        for index, uploaded_file in enumerate(uploaded_files):
            old_filename = uploaded_file.name
            base_name, extension = os.path.splitext(old_filename)
            time.sleep(1)
            timestamp = int(time.time())
            new_filename = f'{site_name}_{types}_{timestamp}{extension}'
            file_path = os.path.join(target_directory, new_filename)
            print(file_path)
            with open(file_path, 'wb') as f:
                f.write(uploaded_file.read())

            st.success(f'成功上传并重命名 {len(uploaded_files)} 个文件到 {target_directory}。')

        # 添加下载按钮
        if st.button('下载所有文件'):
            zip_filename = site_name + '.zip'
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for root, dirs, files in os.walk(target_directory):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, target_directory))

            with open(zip_filename, 'rb') as f:
                bytes_data = f.read()
                st.download_button(label='点击下载', data=bytes_data, file_name=zip_filename)
