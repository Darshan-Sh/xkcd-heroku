import re,requests,bs4,shutil,os

ImgURLReg = re.compile(r'src="([^"]*)"')

for i in range(20):

    #Get the image selector
    XKCDPage = requests.get(r'https://c.xkcd.com/random/comic/')
    XKCDsoup = bs4.BeautifulSoup(XKCDPage.text,'html.parser')
    ImgElem = XKCDsoup.select('#comic > img')

    #Get the Img Link from the selector
    ImgURL =ImgURLReg.findall(str(ImgElem[0]))
    ImgURL = 'https:' + ImgURL[0]

    #Download the image
    Img = requests.get(ImgURL,stream = True)
    if Img.status_code == 200:
        Img.raw.decode_content = True
        FileName = ImgURL.split(r'/')[-1]
        File = open(FileName,'wb')
        shutil.copyfileobj(Img.raw,File)
        File.close()
        if os.path.getsize(FileName) != 0:
            print('Image: %s got downloaded!' %(FileName))
    else:
        print('Did not get image')

