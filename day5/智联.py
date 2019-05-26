import requests


headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,images/webp,images/apng,*/*;q=0.8",
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',

}


def getcitycode():
    cityname = input('请输入你要查询的城市：')
    url = 'https://fe-api.zhaopin.com/c/i/city-page/user-city?ipCity='+cityname
    response = requests.get(url)
    response.encoding = 'utf8'
    result = response.json()
    cityid = result['data']['code']
    return cityid
def getjobs():
    citycode = getcitycode()
    kw = input('请输入你需要的工作关键字:')
    pages = int(input('请输入你需要前多少页工作信息:'))
    for page in range(0,pages):
        url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(page*60)+'&pageSize=60&cityId='+citycode+'&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw='+kw+'&kt=3'
        response = requests.get(url,headers=headers)
        response.encoding = 'utf8'
        result = response.json()
        resultlist = result['data']['results']
        for job in resultlist:
            companyName = job['company']['name']
            jobName = job['jobName']
            jobSalary = job['salary']
            eduLevel = job['eduLevel']['name']
            jobWelfare = job['welfare']
            print(companyName,jobName,jobSalary,eduLevel,jobWelfare)
        print('*'*100)

getjobs()
