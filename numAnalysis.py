import urllib.request

webUrl = 'https://www.flalottery.com/exptkt/mmil.htm'

getWebData = urllib.request.urlopen(webUrl)

rWebData = getWebData.read() #read the html file
#print(x)

crfile = open('fllottery.html','wb+').write(rWebData)
#crfile.write(getWebData)

#next step: write the file to a .txt file locally
#crfile = open('fllottery.txt','wb+').write(rrWebData)

