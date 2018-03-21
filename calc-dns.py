import os
def main():	
	url = ['suoidet', 'salas', 'emirpdio', 'phoenix', 'presstiege', 'guccigav', 'sdbrown', 'alphasqd', 'mrchin', 'obajedi', 'mosswine', 'deviljho', 'richard2', 'higley', 'brandon50', 'kevinf42']
	ip = ['10.183.1.1', '10.183.1.2', '10.183.1.3', '10.183.1.4', '10.183.1.7', '10.183.1.8', '10.183.1.9', '10.183.1.10', '10.183.1.11', '10.183.1.12', '10.183.1.13', '10.183.1.14', '10.183.1.15', '10.183.1.16', '10.183.1.18', '10.183.1.19']
	print (url)
	print(ip)
	for i in  range (0, 16):
		urlstring1 = url[i]+'.ioe'
		urlstring2 = 'www.'+url[i]+'.ioe'
		urlstring3 = 'video.'+url[i]+'.ioe'
		cmd0 = 'touch '+ urlstring1
		os.system(cmd0)
		echo1 = 'address=/'+urlstring1+'/'+ip[i]
		echo2 = 'address=/'+urlstring2+'/'+ip[i]
		echo3 = 'address=/'+urlstring3+'/'+ip[i]
		cmd1 = 'echo "'+echo1+'" >>'+urlstring1
		cmd2 = 'echo "'+echo2+'" >>'+urlstring1
		cmd3 = 'echo "'+echo3+'" >>'+urlstring1
		print(cmd1)
		print(cmd2)
		print(cmd3)
		os.system(cmd1)
		os.system(cmd2)
		os.system(cmd3)

main()


#address=/icebowl.ioe/10.183.1.30
#address=/www.icebowl.ioe/10.183.1.30
#address=/ftp.icebowl.ioe/10.183.1.30
#address=/video.icebowl.ioe/10.183.1.30

#1* 10.183.1.1 * suoidet.ioe * 0 *
#2* 10.183.1.2 * salas.ioe * 0 *
#3* 10.183.1.3 * emirpdio.ioe * 0 * 
#4* 10.183.1.4 * phoenix.ioe * 0 * 
#5* 10.183.1.7 * prestige.ioe * 0 * 
#6* 10.183.1.8 * guccigav.ioe * 0 * 
#7* 10.183.1.9 * sdbrown.ioe * 0 * 
#8* 10.183.1.10 * ballin.ioe * 0 * 
#9* 10.183.1.11 * mrchin.ioe * 0 * 
#10* 10.183.1.12 * obdajedi.ioe * 0 * 
#11* 10.183.1.13 * mosswine.ioe * 0 * 
#12* 10.183.1.14 * deviljho.ioe * 0 *
#13 * 10.183.1.15 * richard2.ioe * 0 * 
#14 * 10.183.1.16 * higley.ioe * 0 * 
#15* 10.183.1.18 * brandon50.ioe * 0 * 
#16* 10.183.1.19 * KevinF42.ioe * 0 * 

 
