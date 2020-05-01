import unittest

from project1 import main

class OutPutTestCase(unittest.TestCase):

    def test_mn(self):
        mn,mx,avg,std,cor = main('project/sample_student_marks.csv')
        print(mn)
        self.assertEqual(mn,[0.0, 6.0, 3.0, 5.0, 1.0, 7.0, 9.0, 2.0, 262.0])
    
    def test_mx(self):
        mn,mx,avg,std,cor = main('project/sample_student_marks.csv')
        print(mx)
        self.assertEqual(mx,[98.0, 96.0, 92.0, 92.0, 96.0, 97.0, 94.0, 100.0, 587.0])
    
    def test_avg(self):
        mn,mx,avg,std,cor = main('project/sample_student_marks.csv')
        print(avg)
        self.assertEqual(avg,[49.7667, 53.2333, 61.7333, 54.6333, 57.2333, 55.0, 50.5, 43.0, 425.1])

    def test_std(self):
        mn,mx,avg,std,cor = main('project/sample_student_marks.csv')
        print(std)
        self.assertEqual(std,[31.3706, 24.5678, 25.737, 26.1731, 31.6014, 27.3496, 23.8841, 30.7864, 83.7661])
    
    def test_cor(self):
        mn,mx,avg,std,cor = main('project/sample_student_marks.csv')
        print(cor)
        self.assertEqual(cor,[0.2622, 0.2733, 0.3293, 0.3451, 0.4058, 0.2747, 0.4258, 0.4871, 1.0])


    ##ReOrder of sample 1

    def test_mn1(self):
        mn,mx,avg,std,cor = main('project/test1.csv')
        print(mn)
        self.assertEqual(mn,[0.0, 6.0, 3.0, 5.0, 1.0, 7.0, 9.0, 2.0, 262.0])
    
    def test_mx1(self):
        mn,mx,avg,std,cor = main('project/test1.csv')
        print(mx)
        self.assertEqual(mx,[98.0, 96.0, 92.0, 92.0, 96.0, 97.0, 94.0, 100.0, 587.0])
    
    def test_avg1(self):
        mn,mx,avg,std,cor = main('project/test1.csv')
        print(avg)
        self.assertEqual(avg,[49.7667, 53.2333, 61.7333, 54.6333, 57.2333, 55.0, 50.5, 43.0, 425.1])

    def test_std1(self):
        mn,mx,avg,std,cor = main('project/test1.csv')
        print(std)
        self.assertEqual(std,[31.3706, 24.5678, 25.737, 26.1731, 31.6014, 27.3496, 23.8841, 30.7864, 83.7661])
    
    def test_cor1(self):
        mn,mx,avg,std,cor = main('project/test1.csv')
        print(cor)
        self.assertEqual(cor,[0.2622, 0.2733, 0.3293, 0.3451, 0.4058, 0.2747, 0.4258, 0.4871, 1.0])
    
    ## Reorder Sample 2

    def test_mn2(self):
        mn,mx,avg,std,cor = main('project/test2.csv')
        print(mn)
        self.assertEqual(mn,[0.0, 6.0, 3.0, 5.0, 1.0, 7.0, 9.0, 2.0, 262.0])
    
    def test_mx2(self):
        mn,mx,avg,std,cor = main('project/test2.csv')
        print(mx)
        self.assertEqual(mx,[98.0, 96.0, 92.0, 92.0, 96.0, 97.0, 94.0, 100.0, 587.0])
    
    def test_avg2(self):
        mn,mx,avg,std,cor = main('project/test2.csv')
        print(avg)
        self.assertEqual(avg,[49.7667, 53.2333, 61.7333, 54.6333, 57.2333, 55.0, 50.5, 43.0, 425.1])

    def test_std2(self):
        mn,mx,avg,std,cor = main('project/test2.csv')
        print(std)
        self.assertEqual(std,[31.3706, 24.5678, 25.737, 26.1731, 31.6014, 27.3496, 23.8841, 30.7864, 83.7661])
    
    def test_cor2(self):
        mn,mx,avg,std,cor = main('project/test2.csv')
        print(cor)
        self.assertEqual(cor,[0.2622, 0.2733, 0.3293, 0.3451, 0.4058, 0.2747, 0.4258, 0.4871, 1.0])
    
    def test_cor3(self):
        mn,mx,avg,std,cor = main('project/test2.csv')
        print(mn,mx,avg,std,cor)
    