import unittest

# Define the function to be tested
def parse_code_og(a,b,c,d,aa,bb,cc,ccc,bbb,bbbb):
   out = ""
   if a:
      out += ('.a')
      if aa:
         out += ('.aa')
      else:
         out += ('.-aa')
      #endif
      out += ('.a')
   elif b:
      out += ('.b')
      if bb:
         out += ('.bb')
      elif bbb:
         out += ('.bbb')
      elif bbbb:
         out += ('.bbbb')
      #endif
      out += ('.b')
   elif c:
      out += ('.c')
      if cc:
         out += ('.cc')
      elif ccc:
         out += ('.ccc')         
      else:
         out += ('.-cc-ccc')
      #endif
      out += ('.c')
   else:
      out += ('.-a-b-c')
      if d:
         out += ('.d')    
      #endif  
      out += ('.-a-b-c')
   #endif
   out += ('.0')
   return out

def test_code_py(a,b,c,d,aa,bb,cc,bbb,ccc,bbbb):
    if 1 == 1: out = ""
    if a: out += ('.a')
    if a and aa: out += ('.aa')
    if a and not (aa): out += ('.-aa')
    if a: out += ('.a')
    if b and not (a): out += ('.b')
    if b and bb and not (a): out += ('.bb')
    if b and bbb and not (a or bb): out += ('.bbb')
    if b and bbbb and not (a or bb or bbb): out += ('.bbbb')
    if b and not (a): out += ('.b')
    if c and not (a or b): out += ('.c')
    if c and cc and not (a or b): out += ('.cc')
    if c and ccc and not (a or b or cc): out += ('.ccc')
    if c and not (a or b or cc or ccc): out += ('.-cc-ccc')
    if c and not (a or b): out += ('.c')
    if not (a or b or c): out += ('.-a-b-c')
    if d and not (a or b or c): out += ('.d')
    if not (a or b or c): out += ('.-a-b-c')
    if 1 == 1: out += ('.0')
    if 1 == 1: return out

# Create a test class that inherits from unittest.TestCase
class TestElseif(unittest.TestCase):
    # Test 0"
    def test_case_0(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 1"
    def test_case_1(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 2"
    def test_case_2(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 3"
    def test_case_3(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 4"
    def test_case_4(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 5"
    def test_case_5(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 6"
    def test_case_6(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 7"
    def test_case_7(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 8"
    def test_case_8(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 9"
    def test_case_9(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 10"
    def test_case_10(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 11"
    def test_case_11(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 12"
    def test_case_12(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 13"
    def test_case_13(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 14"
    def test_case_14(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 15"
    def test_case_15(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 16"
    def test_case_16(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 17"
    def test_case_17(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 18"
    def test_case_18(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 19"
    def test_case_19(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 20"
    def test_case_20(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 21"
    def test_case_21(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 22"
    def test_case_22(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 23"
    def test_case_23(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 24"
    def test_case_24(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 25"
    def test_case_25(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 26"
    def test_case_26(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 27"
    def test_case_27(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 28"
    def test_case_28(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 29"
    def test_case_29(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 30"
    def test_case_30(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 31"
    def test_case_31(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 32"
    def test_case_32(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 33"
    def test_case_33(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 34"
    def test_case_34(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 35"
    def test_case_35(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 36"
    def test_case_36(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 37"
    def test_case_37(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 38"
    def test_case_38(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 39"
    def test_case_39(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 40"
    def test_case_40(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 41"
    def test_case_41(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 42"
    def test_case_42(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 43"
    def test_case_43(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 44"
    def test_case_44(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 45"
    def test_case_45(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 46"
    def test_case_46(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 47"
    def test_case_47(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 48"
    def test_case_48(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 49"
    def test_case_49(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 50"
    def test_case_50(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 51"
    def test_case_51(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 52"
    def test_case_52(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 53"
    def test_case_53(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 54"
    def test_case_54(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 55"
    def test_case_55(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 56"
    def test_case_56(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 57"
    def test_case_57(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 58"
    def test_case_58(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 59"
    def test_case_59(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 60"
    def test_case_60(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 61"
    def test_case_61(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 62"
    def test_case_62(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 63"
    def test_case_63(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 64"
    def test_case_64(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 65"
    def test_case_65(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 66"
    def test_case_66(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 67"
    def test_case_67(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 68"
    def test_case_68(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 69"
    def test_case_69(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 70"
    def test_case_70(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 71"
    def test_case_71(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 72"
    def test_case_72(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 73"
    def test_case_73(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 74"
    def test_case_74(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 75"
    def test_case_75(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 76"
    def test_case_76(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 77"
    def test_case_77(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 78"
    def test_case_78(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 79"
    def test_case_79(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 80"
    def test_case_80(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 81"
    def test_case_81(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 82"
    def test_case_82(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 83"
    def test_case_83(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 84"
    def test_case_84(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 85"
    def test_case_85(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 86"
    def test_case_86(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 87"
    def test_case_87(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 88"
    def test_case_88(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 89"
    def test_case_89(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 90"
    def test_case_90(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 91"
    def test_case_91(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 92"
    def test_case_92(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 93"
    def test_case_93(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 94"
    def test_case_94(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 95"
    def test_case_95(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 96"
    def test_case_96(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 97"
    def test_case_97(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 98"
    def test_case_98(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 99"
    def test_case_99(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 100"
    def test_case_100(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 101"
    def test_case_101(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 102"
    def test_case_102(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 103"
    def test_case_103(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 104"
    def test_case_104(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 105"
    def test_case_105(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 106"
    def test_case_106(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 107"
    def test_case_107(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 108"
    def test_case_108(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 109"
    def test_case_109(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 110"
    def test_case_110(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 111"
    def test_case_111(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 112"
    def test_case_112(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 113"
    def test_case_113(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 114"
    def test_case_114(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 115"
    def test_case_115(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 116"
    def test_case_116(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 117"
    def test_case_117(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 118"
    def test_case_118(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 119"
    def test_case_119(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 120"
    def test_case_120(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 121"
    def test_case_121(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 122"
    def test_case_122(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 123"
    def test_case_123(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 124"
    def test_case_124(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 125"
    def test_case_125(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 126"
    def test_case_126(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 127"
    def test_case_127(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 128"
    def test_case_128(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 129"
    def test_case_129(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 130"
    def test_case_130(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 131"
    def test_case_131(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 132"
    def test_case_132(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 133"
    def test_case_133(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 134"
    def test_case_134(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 135"
    def test_case_135(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 136"
    def test_case_136(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 137"
    def test_case_137(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 138"
    def test_case_138(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 139"
    def test_case_139(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 140"
    def test_case_140(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 141"
    def test_case_141(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 142"
    def test_case_142(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 143"
    def test_case_143(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 144"
    def test_case_144(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 145"
    def test_case_145(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 146"
    def test_case_146(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 147"
    def test_case_147(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 148"
    def test_case_148(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 149"
    def test_case_149(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 150"
    def test_case_150(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 151"
    def test_case_151(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 152"
    def test_case_152(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 153"
    def test_case_153(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 154"
    def test_case_154(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 155"
    def test_case_155(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 156"
    def test_case_156(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 157"
    def test_case_157(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 158"
    def test_case_158(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 159"
    def test_case_159(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 160"
    def test_case_160(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 161"
    def test_case_161(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 162"
    def test_case_162(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 163"
    def test_case_163(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 164"
    def test_case_164(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 165"
    def test_case_165(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 166"
    def test_case_166(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 167"
    def test_case_167(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 168"
    def test_case_168(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 169"
    def test_case_169(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 170"
    def test_case_170(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 171"
    def test_case_171(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 172"
    def test_case_172(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 173"
    def test_case_173(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 174"
    def test_case_174(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 175"
    def test_case_175(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 176"
    def test_case_176(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 177"
    def test_case_177(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 178"
    def test_case_178(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 179"
    def test_case_179(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 180"
    def test_case_180(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 181"
    def test_case_181(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 182"
    def test_case_182(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 183"
    def test_case_183(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 184"
    def test_case_184(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 185"
    def test_case_185(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 186"
    def test_case_186(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 187"
    def test_case_187(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 188"
    def test_case_188(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 189"
    def test_case_189(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 190"
    def test_case_190(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 191"
    def test_case_191(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 192"
    def test_case_192(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 193"
    def test_case_193(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 194"
    def test_case_194(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 195"
    def test_case_195(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 196"
    def test_case_196(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 197"
    def test_case_197(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 198"
    def test_case_198(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 199"
    def test_case_199(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 200"
    def test_case_200(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 201"
    def test_case_201(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 202"
    def test_case_202(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 203"
    def test_case_203(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 204"
    def test_case_204(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 205"
    def test_case_205(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 206"
    def test_case_206(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 207"
    def test_case_207(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 208"
    def test_case_208(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 209"
    def test_case_209(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 210"
    def test_case_210(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 211"
    def test_case_211(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 212"
    def test_case_212(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 213"
    def test_case_213(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 214"
    def test_case_214(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 215"
    def test_case_215(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 216"
    def test_case_216(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 217"
    def test_case_217(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 218"
    def test_case_218(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 219"
    def test_case_219(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 220"
    def test_case_220(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 221"
    def test_case_221(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 222"
    def test_case_222(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 223"
    def test_case_223(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 224"
    def test_case_224(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 225"
    def test_case_225(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 226"
    def test_case_226(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 227"
    def test_case_227(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 228"
    def test_case_228(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 229"
    def test_case_229(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 230"
    def test_case_230(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 231"
    def test_case_231(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 232"
    def test_case_232(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 233"
    def test_case_233(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 234"
    def test_case_234(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 235"
    def test_case_235(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 236"
    def test_case_236(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 237"
    def test_case_237(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 238"
    def test_case_238(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 239"
    def test_case_239(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 240"
    def test_case_240(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 241"
    def test_case_241(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 242"
    def test_case_242(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 243"
    def test_case_243(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 244"
    def test_case_244(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 245"
    def test_case_245(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 246"
    def test_case_246(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 247"
    def test_case_247(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 248"
    def test_case_248(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 249"
    def test_case_249(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 250"
    def test_case_250(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 251"
    def test_case_251(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 252"
    def test_case_252(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 253"
    def test_case_253(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 254"
    def test_case_254(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 255"
    def test_case_255(self):
        self.assertEqual(parse_code_og(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 256"
    def test_case_256(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 257"
    def test_case_257(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 258"
    def test_case_258(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 259"
    def test_case_259(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 260"
    def test_case_260(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 261"
    def test_case_261(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 262"
    def test_case_262(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 263"
    def test_case_263(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 264"
    def test_case_264(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 265"
    def test_case_265(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 266"
    def test_case_266(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 267"
    def test_case_267(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 268"
    def test_case_268(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 269"
    def test_case_269(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 270"
    def test_case_270(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 271"
    def test_case_271(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 272"
    def test_case_272(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 273"
    def test_case_273(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 274"
    def test_case_274(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 275"
    def test_case_275(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 276"
    def test_case_276(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 277"
    def test_case_277(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 278"
    def test_case_278(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 279"
    def test_case_279(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 280"
    def test_case_280(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 281"
    def test_case_281(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 282"
    def test_case_282(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 283"
    def test_case_283(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 284"
    def test_case_284(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 285"
    def test_case_285(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 286"
    def test_case_286(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 287"
    def test_case_287(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 288"
    def test_case_288(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 289"
    def test_case_289(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 290"
    def test_case_290(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 291"
    def test_case_291(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 292"
    def test_case_292(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 293"
    def test_case_293(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 294"
    def test_case_294(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 295"
    def test_case_295(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 296"
    def test_case_296(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 297"
    def test_case_297(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 298"
    def test_case_298(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 299"
    def test_case_299(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 300"
    def test_case_300(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 301"
    def test_case_301(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 302"
    def test_case_302(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 303"
    def test_case_303(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 304"
    def test_case_304(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 305"
    def test_case_305(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 306"
    def test_case_306(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 307"
    def test_case_307(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 308"
    def test_case_308(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 309"
    def test_case_309(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 310"
    def test_case_310(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 311"
    def test_case_311(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 312"
    def test_case_312(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 313"
    def test_case_313(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 314"
    def test_case_314(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 315"
    def test_case_315(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 316"
    def test_case_316(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 317"
    def test_case_317(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 318"
    def test_case_318(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 319"
    def test_case_319(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 320"
    def test_case_320(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 321"
    def test_case_321(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 322"
    def test_case_322(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 323"
    def test_case_323(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 324"
    def test_case_324(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 325"
    def test_case_325(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 326"
    def test_case_326(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 327"
    def test_case_327(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 328"
    def test_case_328(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 329"
    def test_case_329(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 330"
    def test_case_330(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 331"
    def test_case_331(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 332"
    def test_case_332(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 333"
    def test_case_333(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 334"
    def test_case_334(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 335"
    def test_case_335(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 336"
    def test_case_336(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 337"
    def test_case_337(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 338"
    def test_case_338(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 339"
    def test_case_339(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 340"
    def test_case_340(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 341"
    def test_case_341(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 342"
    def test_case_342(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 343"
    def test_case_343(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 344"
    def test_case_344(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 345"
    def test_case_345(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 346"
    def test_case_346(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 347"
    def test_case_347(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 348"
    def test_case_348(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 349"
    def test_case_349(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 350"
    def test_case_350(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 351"
    def test_case_351(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 352"
    def test_case_352(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 353"
    def test_case_353(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 354"
    def test_case_354(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 355"
    def test_case_355(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 356"
    def test_case_356(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 357"
    def test_case_357(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 358"
    def test_case_358(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 359"
    def test_case_359(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 360"
    def test_case_360(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 361"
    def test_case_361(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 362"
    def test_case_362(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 363"
    def test_case_363(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 364"
    def test_case_364(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 365"
    def test_case_365(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 366"
    def test_case_366(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 367"
    def test_case_367(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 368"
    def test_case_368(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 369"
    def test_case_369(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 370"
    def test_case_370(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 371"
    def test_case_371(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 372"
    def test_case_372(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 373"
    def test_case_373(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 374"
    def test_case_374(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 375"
    def test_case_375(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 376"
    def test_case_376(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 377"
    def test_case_377(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 378"
    def test_case_378(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 379"
    def test_case_379(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 380"
    def test_case_380(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 381"
    def test_case_381(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 382"
    def test_case_382(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 383"
    def test_case_383(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 384"
    def test_case_384(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 385"
    def test_case_385(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 386"
    def test_case_386(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 387"
    def test_case_387(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 388"
    def test_case_388(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 389"
    def test_case_389(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 390"
    def test_case_390(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 391"
    def test_case_391(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 392"
    def test_case_392(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 393"
    def test_case_393(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 394"
    def test_case_394(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 395"
    def test_case_395(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 396"
    def test_case_396(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 397"
    def test_case_397(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 398"
    def test_case_398(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 399"
    def test_case_399(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 400"
    def test_case_400(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 401"
    def test_case_401(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 402"
    def test_case_402(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 403"
    def test_case_403(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 404"
    def test_case_404(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 405"
    def test_case_405(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 406"
    def test_case_406(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 407"
    def test_case_407(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 408"
    def test_case_408(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 409"
    def test_case_409(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 410"
    def test_case_410(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 411"
    def test_case_411(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 412"
    def test_case_412(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 413"
    def test_case_413(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 414"
    def test_case_414(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 415"
    def test_case_415(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 416"
    def test_case_416(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 417"
    def test_case_417(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 418"
    def test_case_418(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 419"
    def test_case_419(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 420"
    def test_case_420(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 421"
    def test_case_421(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 422"
    def test_case_422(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 423"
    def test_case_423(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 424"
    def test_case_424(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 425"
    def test_case_425(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 426"
    def test_case_426(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 427"
    def test_case_427(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 428"
    def test_case_428(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 429"
    def test_case_429(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 430"
    def test_case_430(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 431"
    def test_case_431(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 432"
    def test_case_432(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 433"
    def test_case_433(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 434"
    def test_case_434(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 435"
    def test_case_435(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 436"
    def test_case_436(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 437"
    def test_case_437(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 438"
    def test_case_438(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 439"
    def test_case_439(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 440"
    def test_case_440(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 441"
    def test_case_441(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 442"
    def test_case_442(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 443"
    def test_case_443(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 444"
    def test_case_444(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 445"
    def test_case_445(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 446"
    def test_case_446(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 447"
    def test_case_447(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 448"
    def test_case_448(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 449"
    def test_case_449(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 450"
    def test_case_450(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 451"
    def test_case_451(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 452"
    def test_case_452(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 453"
    def test_case_453(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 454"
    def test_case_454(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 455"
    def test_case_455(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 456"
    def test_case_456(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 457"
    def test_case_457(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 458"
    def test_case_458(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 459"
    def test_case_459(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 460"
    def test_case_460(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 461"
    def test_case_461(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 462"
    def test_case_462(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 463"
    def test_case_463(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 464"
    def test_case_464(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 465"
    def test_case_465(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 466"
    def test_case_466(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 467"
    def test_case_467(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 468"
    def test_case_468(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 469"
    def test_case_469(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 470"
    def test_case_470(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 471"
    def test_case_471(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 472"
    def test_case_472(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 473"
    def test_case_473(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 474"
    def test_case_474(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 475"
    def test_case_475(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 476"
    def test_case_476(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 477"
    def test_case_477(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 478"
    def test_case_478(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 479"
    def test_case_479(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 480"
    def test_case_480(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 481"
    def test_case_481(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 482"
    def test_case_482(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 483"
    def test_case_483(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 484"
    def test_case_484(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 485"
    def test_case_485(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 486"
    def test_case_486(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 487"
    def test_case_487(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 488"
    def test_case_488(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 489"
    def test_case_489(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 490"
    def test_case_490(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 491"
    def test_case_491(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 492"
    def test_case_492(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 493"
    def test_case_493(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 494"
    def test_case_494(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 495"
    def test_case_495(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 496"
    def test_case_496(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 497"
    def test_case_497(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 498"
    def test_case_498(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 499"
    def test_case_499(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 500"
    def test_case_500(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 501"
    def test_case_501(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 502"
    def test_case_502(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 503"
    def test_case_503(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 504"
    def test_case_504(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 505"
    def test_case_505(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 506"
    def test_case_506(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 507"
    def test_case_507(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 508"
    def test_case_508(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 509"
    def test_case_509(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 510"
    def test_case_510(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 511"
    def test_case_511(self):
        self.assertEqual(parse_code_og(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = False, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 512"
    def test_case_512(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 513"
    def test_case_513(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 514"
    def test_case_514(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 515"
    def test_case_515(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 516"
    def test_case_516(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 517"
    def test_case_517(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 518"
    def test_case_518(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 519"
    def test_case_519(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 520"
    def test_case_520(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 521"
    def test_case_521(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 522"
    def test_case_522(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 523"
    def test_case_523(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 524"
    def test_case_524(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 525"
    def test_case_525(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 526"
    def test_case_526(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 527"
    def test_case_527(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 528"
    def test_case_528(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 529"
    def test_case_529(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 530"
    def test_case_530(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 531"
    def test_case_531(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 532"
    def test_case_532(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 533"
    def test_case_533(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 534"
    def test_case_534(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 535"
    def test_case_535(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 536"
    def test_case_536(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 537"
    def test_case_537(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 538"
    def test_case_538(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 539"
    def test_case_539(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 540"
    def test_case_540(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 541"
    def test_case_541(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 542"
    def test_case_542(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 543"
    def test_case_543(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 544"
    def test_case_544(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 545"
    def test_case_545(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 546"
    def test_case_546(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 547"
    def test_case_547(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 548"
    def test_case_548(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 549"
    def test_case_549(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 550"
    def test_case_550(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 551"
    def test_case_551(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 552"
    def test_case_552(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 553"
    def test_case_553(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 554"
    def test_case_554(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 555"
    def test_case_555(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 556"
    def test_case_556(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 557"
    def test_case_557(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 558"
    def test_case_558(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 559"
    def test_case_559(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 560"
    def test_case_560(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 561"
    def test_case_561(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 562"
    def test_case_562(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 563"
    def test_case_563(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 564"
    def test_case_564(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 565"
    def test_case_565(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 566"
    def test_case_566(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 567"
    def test_case_567(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 568"
    def test_case_568(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 569"
    def test_case_569(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 570"
    def test_case_570(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 571"
    def test_case_571(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 572"
    def test_case_572(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 573"
    def test_case_573(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 574"
    def test_case_574(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 575"
    def test_case_575(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 576"
    def test_case_576(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 577"
    def test_case_577(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 578"
    def test_case_578(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 579"
    def test_case_579(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 580"
    def test_case_580(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 581"
    def test_case_581(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 582"
    def test_case_582(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 583"
    def test_case_583(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 584"
    def test_case_584(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 585"
    def test_case_585(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 586"
    def test_case_586(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 587"
    def test_case_587(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 588"
    def test_case_588(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 589"
    def test_case_589(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 590"
    def test_case_590(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 591"
    def test_case_591(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 592"
    def test_case_592(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 593"
    def test_case_593(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 594"
    def test_case_594(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 595"
    def test_case_595(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 596"
    def test_case_596(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 597"
    def test_case_597(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 598"
    def test_case_598(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 599"
    def test_case_599(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 600"
    def test_case_600(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 601"
    def test_case_601(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 602"
    def test_case_602(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 603"
    def test_case_603(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 604"
    def test_case_604(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 605"
    def test_case_605(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 606"
    def test_case_606(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 607"
    def test_case_607(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 608"
    def test_case_608(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 609"
    def test_case_609(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 610"
    def test_case_610(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 611"
    def test_case_611(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 612"
    def test_case_612(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 613"
    def test_case_613(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 614"
    def test_case_614(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 615"
    def test_case_615(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 616"
    def test_case_616(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 617"
    def test_case_617(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 618"
    def test_case_618(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 619"
    def test_case_619(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 620"
    def test_case_620(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 621"
    def test_case_621(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 622"
    def test_case_622(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 623"
    def test_case_623(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 624"
    def test_case_624(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 625"
    def test_case_625(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 626"
    def test_case_626(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 627"
    def test_case_627(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 628"
    def test_case_628(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 629"
    def test_case_629(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 630"
    def test_case_630(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 631"
    def test_case_631(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 632"
    def test_case_632(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 633"
    def test_case_633(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 634"
    def test_case_634(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 635"
    def test_case_635(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 636"
    def test_case_636(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 637"
    def test_case_637(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 638"
    def test_case_638(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 639"
    def test_case_639(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 640"
    def test_case_640(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 641"
    def test_case_641(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 642"
    def test_case_642(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 643"
    def test_case_643(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 644"
    def test_case_644(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 645"
    def test_case_645(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 646"
    def test_case_646(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 647"
    def test_case_647(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 648"
    def test_case_648(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 649"
    def test_case_649(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 650"
    def test_case_650(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 651"
    def test_case_651(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 652"
    def test_case_652(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 653"
    def test_case_653(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 654"
    def test_case_654(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 655"
    def test_case_655(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 656"
    def test_case_656(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 657"
    def test_case_657(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 658"
    def test_case_658(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 659"
    def test_case_659(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 660"
    def test_case_660(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 661"
    def test_case_661(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 662"
    def test_case_662(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 663"
    def test_case_663(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 664"
    def test_case_664(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 665"
    def test_case_665(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 666"
    def test_case_666(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 667"
    def test_case_667(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 668"
    def test_case_668(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 669"
    def test_case_669(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 670"
    def test_case_670(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 671"
    def test_case_671(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 672"
    def test_case_672(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 673"
    def test_case_673(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 674"
    def test_case_674(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 675"
    def test_case_675(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 676"
    def test_case_676(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 677"
    def test_case_677(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 678"
    def test_case_678(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 679"
    def test_case_679(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 680"
    def test_case_680(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 681"
    def test_case_681(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 682"
    def test_case_682(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 683"
    def test_case_683(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 684"
    def test_case_684(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 685"
    def test_case_685(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 686"
    def test_case_686(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 687"
    def test_case_687(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 688"
    def test_case_688(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 689"
    def test_case_689(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 690"
    def test_case_690(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 691"
    def test_case_691(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 692"
    def test_case_692(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 693"
    def test_case_693(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 694"
    def test_case_694(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 695"
    def test_case_695(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 696"
    def test_case_696(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 697"
    def test_case_697(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 698"
    def test_case_698(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 699"
    def test_case_699(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 700"
    def test_case_700(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 701"
    def test_case_701(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 702"
    def test_case_702(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 703"
    def test_case_703(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 704"
    def test_case_704(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 705"
    def test_case_705(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 706"
    def test_case_706(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 707"
    def test_case_707(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 708"
    def test_case_708(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 709"
    def test_case_709(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 710"
    def test_case_710(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 711"
    def test_case_711(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 712"
    def test_case_712(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 713"
    def test_case_713(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 714"
    def test_case_714(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 715"
    def test_case_715(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 716"
    def test_case_716(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 717"
    def test_case_717(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 718"
    def test_case_718(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 719"
    def test_case_719(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 720"
    def test_case_720(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 721"
    def test_case_721(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 722"
    def test_case_722(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 723"
    def test_case_723(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 724"
    def test_case_724(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 725"
    def test_case_725(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 726"
    def test_case_726(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 727"
    def test_case_727(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 728"
    def test_case_728(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 729"
    def test_case_729(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 730"
    def test_case_730(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 731"
    def test_case_731(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 732"
    def test_case_732(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 733"
    def test_case_733(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 734"
    def test_case_734(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 735"
    def test_case_735(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 736"
    def test_case_736(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 737"
    def test_case_737(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 738"
    def test_case_738(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 739"
    def test_case_739(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 740"
    def test_case_740(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 741"
    def test_case_741(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 742"
    def test_case_742(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 743"
    def test_case_743(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 744"
    def test_case_744(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 745"
    def test_case_745(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 746"
    def test_case_746(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 747"
    def test_case_747(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 748"
    def test_case_748(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 749"
    def test_case_749(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 750"
    def test_case_750(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 751"
    def test_case_751(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 752"
    def test_case_752(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 753"
    def test_case_753(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 754"
    def test_case_754(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 755"
    def test_case_755(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 756"
    def test_case_756(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 757"
    def test_case_757(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 758"
    def test_case_758(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 759"
    def test_case_759(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 760"
    def test_case_760(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 761"
    def test_case_761(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 762"
    def test_case_762(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 763"
    def test_case_763(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 764"
    def test_case_764(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 765"
    def test_case_765(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 766"
    def test_case_766(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 767"
    def test_case_767(self):
        self.assertEqual(parse_code_og(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = False, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 768"
    def test_case_768(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 769"
    def test_case_769(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 770"
    def test_case_770(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 771"
    def test_case_771(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 772"
    def test_case_772(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 773"
    def test_case_773(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 774"
    def test_case_774(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 775"
    def test_case_775(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 776"
    def test_case_776(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 777"
    def test_case_777(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 778"
    def test_case_778(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 779"
    def test_case_779(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 780"
    def test_case_780(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 781"
    def test_case_781(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 782"
    def test_case_782(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 783"
    def test_case_783(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 784"
    def test_case_784(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 785"
    def test_case_785(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 786"
    def test_case_786(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 787"
    def test_case_787(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 788"
    def test_case_788(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 789"
    def test_case_789(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 790"
    def test_case_790(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 791"
    def test_case_791(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 792"
    def test_case_792(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 793"
    def test_case_793(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 794"
    def test_case_794(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 795"
    def test_case_795(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 796"
    def test_case_796(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 797"
    def test_case_797(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 798"
    def test_case_798(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 799"
    def test_case_799(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 800"
    def test_case_800(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 801"
    def test_case_801(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 802"
    def test_case_802(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 803"
    def test_case_803(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 804"
    def test_case_804(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 805"
    def test_case_805(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 806"
    def test_case_806(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 807"
    def test_case_807(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 808"
    def test_case_808(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 809"
    def test_case_809(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 810"
    def test_case_810(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 811"
    def test_case_811(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 812"
    def test_case_812(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 813"
    def test_case_813(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 814"
    def test_case_814(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 815"
    def test_case_815(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 816"
    def test_case_816(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 817"
    def test_case_817(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 818"
    def test_case_818(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 819"
    def test_case_819(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 820"
    def test_case_820(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 821"
    def test_case_821(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 822"
    def test_case_822(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 823"
    def test_case_823(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 824"
    def test_case_824(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 825"
    def test_case_825(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 826"
    def test_case_826(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 827"
    def test_case_827(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 828"
    def test_case_828(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 829"
    def test_case_829(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 830"
    def test_case_830(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 831"
    def test_case_831(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 832"
    def test_case_832(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 833"
    def test_case_833(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 834"
    def test_case_834(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 835"
    def test_case_835(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 836"
    def test_case_836(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 837"
    def test_case_837(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 838"
    def test_case_838(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 839"
    def test_case_839(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 840"
    def test_case_840(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 841"
    def test_case_841(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 842"
    def test_case_842(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 843"
    def test_case_843(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 844"
    def test_case_844(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 845"
    def test_case_845(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 846"
    def test_case_846(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 847"
    def test_case_847(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 848"
    def test_case_848(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 849"
    def test_case_849(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 850"
    def test_case_850(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 851"
    def test_case_851(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 852"
    def test_case_852(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 853"
    def test_case_853(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 854"
    def test_case_854(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 855"
    def test_case_855(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 856"
    def test_case_856(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 857"
    def test_case_857(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 858"
    def test_case_858(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 859"
    def test_case_859(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 860"
    def test_case_860(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 861"
    def test_case_861(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 862"
    def test_case_862(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 863"
    def test_case_863(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 864"
    def test_case_864(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 865"
    def test_case_865(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 866"
    def test_case_866(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 867"
    def test_case_867(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 868"
    def test_case_868(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 869"
    def test_case_869(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 870"
    def test_case_870(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 871"
    def test_case_871(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 872"
    def test_case_872(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 873"
    def test_case_873(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 874"
    def test_case_874(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 875"
    def test_case_875(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 876"
    def test_case_876(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 877"
    def test_case_877(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 878"
    def test_case_878(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 879"
    def test_case_879(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 880"
    def test_case_880(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 881"
    def test_case_881(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 882"
    def test_case_882(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 883"
    def test_case_883(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 884"
    def test_case_884(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 885"
    def test_case_885(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 886"
    def test_case_886(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 887"
    def test_case_887(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 888"
    def test_case_888(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 889"
    def test_case_889(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 890"
    def test_case_890(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 891"
    def test_case_891(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 892"
    def test_case_892(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 893"
    def test_case_893(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 894"
    def test_case_894(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 895"
    def test_case_895(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = False, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 896"
    def test_case_896(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 897"
    def test_case_897(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 898"
    def test_case_898(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 899"
    def test_case_899(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 900"
    def test_case_900(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 901"
    def test_case_901(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 902"
    def test_case_902(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 903"
    def test_case_903(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 904"
    def test_case_904(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 905"
    def test_case_905(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 906"
    def test_case_906(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 907"
    def test_case_907(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 908"
    def test_case_908(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 909"
    def test_case_909(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 910"
    def test_case_910(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 911"
    def test_case_911(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 912"
    def test_case_912(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 913"
    def test_case_913(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 914"
    def test_case_914(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 915"
    def test_case_915(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 916"
    def test_case_916(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 917"
    def test_case_917(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 918"
    def test_case_918(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 919"
    def test_case_919(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 920"
    def test_case_920(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 921"
    def test_case_921(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 922"
    def test_case_922(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 923"
    def test_case_923(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 924"
    def test_case_924(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 925"
    def test_case_925(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 926"
    def test_case_926(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 927"
    def test_case_927(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 928"
    def test_case_928(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 929"
    def test_case_929(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 930"
    def test_case_930(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 931"
    def test_case_931(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 932"
    def test_case_932(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 933"
    def test_case_933(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 934"
    def test_case_934(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 935"
    def test_case_935(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 936"
    def test_case_936(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 937"
    def test_case_937(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 938"
    def test_case_938(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 939"
    def test_case_939(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 940"
    def test_case_940(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 941"
    def test_case_941(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 942"
    def test_case_942(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 943"
    def test_case_943(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 944"
    def test_case_944(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 945"
    def test_case_945(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 946"
    def test_case_946(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 947"
    def test_case_947(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 948"
    def test_case_948(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 949"
    def test_case_949(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 950"
    def test_case_950(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 951"
    def test_case_951(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 952"
    def test_case_952(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 953"
    def test_case_953(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 954"
    def test_case_954(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 955"
    def test_case_955(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 956"
    def test_case_956(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 957"
    def test_case_957(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 958"
    def test_case_958(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 959"
    def test_case_959(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = False, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 960"
    def test_case_960(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 961"
    def test_case_961(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 962"
    def test_case_962(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 963"
    def test_case_963(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 964"
    def test_case_964(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 965"
    def test_case_965(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 966"
    def test_case_966(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 967"
    def test_case_967(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 968"
    def test_case_968(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 969"
    def test_case_969(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 970"
    def test_case_970(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 971"
    def test_case_971(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 972"
    def test_case_972(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 973"
    def test_case_973(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 974"
    def test_case_974(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 975"
    def test_case_975(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 976"
    def test_case_976(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 977"
    def test_case_977(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 978"
    def test_case_978(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 979"
    def test_case_979(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 980"
    def test_case_980(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 981"
    def test_case_981(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 982"
    def test_case_982(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 983"
    def test_case_983(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 984"
    def test_case_984(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 985"
    def test_case_985(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 986"
    def test_case_986(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 987"
    def test_case_987(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 988"
    def test_case_988(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 989"
    def test_case_989(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 990"
    def test_case_990(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 991"
    def test_case_991(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = False, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 992"
    def test_case_992(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 993"
    def test_case_993(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 994"
    def test_case_994(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 995"
    def test_case_995(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 996"
    def test_case_996(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 997"
    def test_case_997(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 998"
    def test_case_998(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 999"
    def test_case_999(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 1000"
    def test_case_1000(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 1001"
    def test_case_1001(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 1002"
    def test_case_1002(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 1003"
    def test_case_1003(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 1004"
    def test_case_1004(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 1005"
    def test_case_1005(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 1006"
    def test_case_1006(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 1007"
    def test_case_1007(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = False, cc = True, ccc = True, bbb = True, bbbb = True))

    # Test 1008"
    def test_case_1008(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = False))

    # Test 1009"
    def test_case_1009(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = False, bbbb = True))

    # Test 1010"
    def test_case_1010(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = False))

    # Test 1011"
    def test_case_1011(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = False, bbb = True, bbbb = True))

    # Test 1012"
    def test_case_1012(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = False))

    # Test 1013"
    def test_case_1013(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = False, bbbb = True))

    # Test 1014"
    def test_case_1014(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = False))

    # Test 1015"
    def test_case_1015(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = False, ccc = True, bbb = True, bbbb = True))

    # Test 1016"
    def test_case_1016(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = False))

    # Test 1017"
    def test_case_1017(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = False, bbbb = True))

    # Test 1018"
    def test_case_1018(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = False))

    # Test 1019"
    def test_case_1019(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = False, bbb = True, bbbb = True))

    # Test 1020"
    def test_case_1020(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = False))

    # Test 1021"
    def test_case_1021(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = False, bbbb = True))

    # Test 1022"
    def test_case_1022(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = False))

    # Test 1023"
    def test_case_1023(self):
        self.assertEqual(parse_code_og(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True),
                         test_code_py(a = True, b = True, c = True, d = True, aa = True, bb = True, cc = True, ccc = True, bbb = True, bbbb = True))

# Run the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
    