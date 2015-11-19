import unittest, hw1

#def callAPI():
    
 #   my_api_key = '84b98c2d82c32107861f1bd1bf9e79aa8a63a0e940eb8945c6433404df549c77'
 #   mc = mediacloud.api.MediaCloud(my_api_key)
 #   return 1

class APITest(unittest.TestCase):
    def testOne(self):
        res =  hw1.APIcall() 
        self.assertEqual(len(res),2)
        assert res[0] != None
        assert res[1] != None

    

def main():
  unittest.main()
    
    

if __name__ == '__main__':
    main()