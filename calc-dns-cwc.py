import os
def main():	
	url = ['suoidet', 'salas', '']
	ip = ['10.183.1.1', '10.183.1.2', '10.183.1.3', '10.183.1.4', '10.183.1.7', '10.183.1.8', '10.183.1.9', '10.183.1.11', '10.183.1.12', '10.183.1.13', '10.183.1.14', '10.183.1.15', '10.183.1.16', '10.183.1.18', '10.183.1.19']
	print (url)
	print(ip)
	for i in  range (0, 15):
		urlstring1 = url[i]+'.ioe'
		urlstring2 = 'www.'+url[i]+'.ioe'
		urlstring3 = 'video.'+url[i]+'.ioe'
		cmd0 = 'touch '+ urlstring1
		os.system(cmd0)
		echo1 = 'address=/'+urlstring1+'/'+ip[i]
		echo2 = 'address=/'+urlstring2+'/'+ip[i]
		echo3 = 'address=/'+urlstring3+'/'+ip[i]
		echo4 = 'address=/'+urlstring4+'/'+ip[i]
		echo5 = 'address=/'+urlstring5+'/'+ip[i]
		echo6 = 'address=/'+urlstring6+'/'+ip[i]
		echo7 = 'address=/'+urlstring7+'/'+ip[i]
		echo8 = 'address=/'+urlstring8+'/'+ip[i]
		echo9 = 'address=/'+urlstring9+'/'+ip[i]
		#echo10 = 'address=/'+urlstring10+'/'+ip[i]
		echo11 = 'address=/'+urlstring11+'/'+ip[i]
		echo12 = 'address=/'+urlstring12+'/'+ip[i]
		echo13 = 'address=/'+urlstring13+'/'+ip[i]
		echo14 = 'address=/'+urlstring14+'/'+ip[i]
		echo15 = 'address=/'+urlstring15+'/'+ip[i]
		echo16 = 'address=/'+urlstring16+'/'+ip[i]
		cmd1 = 'echo "'+echo1+'" >>'+urlstring1
		cmd2 = 'echo "'+echo2+'" >>'+urlstring1
		cmd3 = 'echo "'+echo3+'" >>'+urlstring1
		cmd4 = 'echo "'+echo4+'" >>'+urlstring1
		cmd5 = 'echo "'+echo5+'" >>'+urlstring1
		cmd6 = 'echo "'+echo6+'" >>'+urlstring1
		cmd7 = 'echo "'+echo7+'" >>'+urlstring1
		cmd8 = 'echo "'+echo8+'" >>'+urlstring1
		cmd9 = 'echo "'+echo9+'" >>'+urlstring1
		cmd10 = 'echo "'+echo10+'" >>'+urlstring1
		cmd11 = 'echo "'+echo11+'" >>'+urlstring1
		cmd12 = 'echo "'+echo12+'" >>'+urlstring1
		cmd13 = 'echo "'+echo13+'" >>'+urlstring1
		cmd14 = 'echo "'+echo14+'" >>'+urlstring1
		cmd15 = 'echo "'+echo15+'" >>'+urlstring1
		cmd16 = 'echo "'+echo16+'" >>'+urlstring1
		print(cmd1)
		print(cmd2)
		print(cmd3)
		print(cmd4)
		print(cmd5)
		print(cmd6)
		print(cmd7)
		print(cmd8)
		print(cmd9)
		#print(cmd10)
		print(cmd11)
		print(cmd12)
		print(cmd13)
		print(cmd14)
		print(cmd15)
		print(cmd16)
		
		os.system(cmd1)
		os.system(cmd2)
		os.system(cmd3)
		os.system(cmd4)
		os.system(cmd5)
		os.system(cmd6)
		os.system(cmd7)
		os.system(cmd8)
		os.system(cmd9)
		#os.system(cmd10)
		os.system(cmd11)
		os.system(cmd12)
		os.system(cmd13)
		os.system(cmd14)
		os.system(cmd15)
		os.system(cmd16)						
main()


#address=/icebowl.ioe/10.183.1.30
#address=/www.icebowl.ioe/10.183.1.30
#address=/ftp.icebowl.ioe/10.183.1.30
#address=/video.icebowl.ioe/10.183.1.30

#10.183.1.1 * suoidet.ioe
#10.183.1.2 * salas.ioe
#10.183.1.3 * emirpdio.ioe
#10.183.1.4 * phoenix.ioe
#10.183.1.7 * prestige.ioe
#10.183.1.8 * guccigav.ioe
#10.183.1.9 * sdbrown.ioe

#10.183.1.11 * mrchin.ioe
#10.183.1.12 * obdajedi.ioe
#10.183.1.13 * mosswine.ioe
#10.183.1.14 * deviljho.ioe
#10.183.1.15 * richard2.ioe
#10.183.1.16 * higley.ioe
#10.183.1.18 * suoidet.ioe
#10.183.1.19 * suoidet.ioe
