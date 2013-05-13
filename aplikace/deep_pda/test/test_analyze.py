'''
Created on 12.5.2013

@author: wendy
'''
import unittest
from .test_case import Test

from gdeep_pda import error

#####################################################################
class TestAnalyze(Test):
    
    path = "test/input/"

    def test(self):
        assert True

    def runAnalyze_ok(self, file, string):
        
        out = self.runApplication(["gdeep_analyze", 
                                   "--input=" + self.path + file, 
                                   "--analyze-string=" + string + "",
                                   "--max-steps=1000"], 
                                  0, 
                                  err = False, 
                                  out = True)
        
        return out

    def runAnalyze_err(self, file, string):
        
        out = self.runApplication(["gdeep_analyze", 
                                   "--input=" + self.path + file, 
                                   "--analyze-string=" + string + "",
                                   "--max-steps=1000"], 
                                  0, 
                                  err = True, 
                                  out = False)
        return out
      
            
    def test_ok_analyze_01(self):
                 
        for string in ("a b c", "a a b b c c", "a a a b b b c c c") :
            self.runAnalyze_ok("test_ok_01", string)

    def test_ok_analyze_02(self):
         
        for string in ("a b c", "a a b b c c", "a a a b b b c c c") :
            self.runAnalyze_ok("test_ok_02", string)
     
    def test_ok_analyze_03(self):
                
        for string in ("á ů ž", "á á ů ů ž ž", "á á á ů ů ů ž ž ž") :
            self.runAnalyze_ok("test_ok_03", string)
     
    def test_ok_analyze_04(self):
        
        for string in ("á ů ž", "á á ů ů ž ž", "á á á ů ů ů ž ž ž") :           
            self.runAnalyze_ok("test_ok_04", string)
 
    def test_ok_analyze_05(self):
        
        for string in ("a b c", "a a b b c c", "a a a b b b c c c") :
            self.runAnalyze_ok("test_ok_05", string)
 
    def test_ok_analyze_06(self):

        for string in ("Agáta Bedřich Cecílie", 
                       "Agáta Agáta Bedřich Bedřich Cecílie Cecílie",
                        "Agáta Agáta Agáta Bedřich Bedřich Bedřich Cecílie Cecílie Cecílie") :
            self.runAnalyze_ok("test_ok_06", string)
         
    def test_ok_analyze_07(self):
        
        for string in ("a b c", "a a b b c c", "a a a b b b c c c") :
            self.runAnalyze_ok("test_ok_07", string)
         
    def test_ok_analyze_08(self):
        self.runAnalyze_ok("test_ok_08", "a a a")
 
    def test_ok_analyze_09(self):
        
        for string in ("á ů ž", "á á ů ů ž ž", "á á á ů ů ů ž ž ž") :
            self.runAnalyze_ok("test_ok_09", string)
            
    def test_ok_analyze_states_01(self):
        self.runAnalyze_ok("test_ok_states_01", "a a a")

    def test_ok_analyze_states_02(self):
        
        for string in ("a b c", "a a b b c c", "a a a b b b c c c") :
            self.runAnalyze_ok("test_ok_states_02", string)
        
    def test_ok_analyze_symbols_01(self):
        self.runAnalyze_ok("test_ok_symbols_01", "a a a")

    def test_ok_analyze_symbols_02(self):        
        for string in ("a b c", "a a b b c c", "a a a b b b c c c") :
            self.runAnalyze_ok("test_ok_symbols_02", string)


#####################################################################

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    
    runner = unittest.TextTestRunner()
    test_suite = TestAnalyze().suite()
    runner.run (test_suite)
    
##################################################################### konec souboru