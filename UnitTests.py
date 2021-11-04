import unittest
from aussage import Aussage
from calculate import evaluateTokenList
from tokenizer import Tokenizer


class AussagenTests(unittest.TestCase):

    def test_create_booleans(self):
        tvalue = Aussage(True)
        fvalue = Aussage(False)
        self.assertTrue(tvalue.value)
        self.assertFalse(fvalue.value)

    def test_create_str_true_false(self):
        tvalue = Aussage("true")
        fvalue = Aussage("false")
        self.assertTrue(tvalue.value)
        self.assertFalse(fvalue.value)

    def test_create_str_w_f(self):
        tvalue = Aussage("w")
        fvalue = Aussage("f")
        self.assertTrue(tvalue.value)
        self.assertFalse(fvalue.value)

    def test_create_str_1_0(self):
        tvalue = Aussage("1")
        fvalue = Aussage("0")
        self.assertTrue(tvalue.value)
        self.assertFalse(fvalue.value)

    def test_string_value_default(self):
        self.test_string_value_binary()

    def test_string_value_binary(self):
        tvalue = Aussage(True)
        tvalue.wertDarstellung = "binär"
        fvalue = Aussage(False)
        fvalue.wertDarstellung = "binär"
        self.assertEqual(tvalue.stringValue(), "1")
        self.assertEqual(fvalue.stringValue(), "0")

    def test_string_value_w_f(self):
        tvalue = Aussage(True)
        tvalue.wertDarstellung = "wf"
        fvalue = Aussage(False)
        fvalue.wertDarstellung = "wf"
        self.assertEqual(tvalue.stringValue(), "w")
        self.assertEqual(fvalue.stringValue(), "f")

    def test_string_value_true_false(self):
        tvalue = Aussage(True)
        tvalue.wertDarstellung = "truefalse"
        fvalue = Aussage(False)
        fvalue.wertDarstellung = "truefalse"
        self.assertEqual(tvalue.stringValue(), "true")
        self.assertEqual(fvalue.stringValue(), "false")

    def test_not(self):
        tvalue = Aussage(True)
        fvalue = Aussage(False)
        self.assertFalse(tvalue.nicht().value)
        self.assertTrue(fvalue.nicht().value)

    def test_and(self):
        tvalue = Aussage(True)
        fvalue = Aussage(False)
        self.assertTrue(tvalue.und(tvalue).value)
        self.assertFalse(tvalue.und(fvalue).value)
        self.assertFalse(fvalue.und(tvalue).value)
        self.assertFalse(fvalue.und(fvalue).value)

    def test_or(self):
        tvalue = Aussage(True)
        fvalue = Aussage(False)
        self.assertTrue(tvalue.oder(tvalue).value)
        self.assertTrue(tvalue.oder(fvalue).value)
        self.assertTrue(fvalue.oder(tvalue).value)
        self.assertFalse(fvalue.oder(fvalue).value)

    def test_xor(self):
        tvalue = Aussage(True)
        fvalue = Aussage(False)
        self.assertFalse(tvalue.xor(tvalue).value)
        self.assertTrue(tvalue.xor(fvalue).value)
        self.assertTrue(fvalue.xor(tvalue).value)
        self.assertFalse(fvalue.xor(fvalue).value)

    def test_implies(self):
        tvalue = Aussage(True)
        fvalue = Aussage(False)
        self.assertTrue(tvalue.folgt(tvalue).value)
        self.assertFalse(tvalue.folgt(fvalue).value)
        self.assertTrue(fvalue.folgt(tvalue).value)
        self.assertTrue(fvalue.folgt(fvalue).value)


class TokenizerTests(unittest.TestCase):

    def test_sequence_1(self):
        value_1 = Aussage(True)
        value_2 = Aussage(False)
        tokenizer = Tokenizer("A und nicht B", True, 2, [value_1, value_2])
        token_list = tokenizer.tokenize()
        self.assertEqual([value_1, "und", "(", "nicht", value_2, ")"], token_list)

    def test_sequence_2(self):
        value_1 = Aussage(True)
        value_2 = Aussage(False)
        tokenizer = Tokenizer("A oder nicht nicht nicht B", True, 2, [value_1, value_2])
        token_list = tokenizer.tokenize()
        self.assertEqual([value_1, "oder", "(", "nicht", "nicht", "nicht", value_2, ")"], token_list)

    def test_sequence_3(self):
        value_1 = Aussage(True)
        value_2 = Aussage(False)
        tokenizer = Tokenizer("nicht A oder (A und nicht B)", True, 2, [value_1, value_2])
        token_list = tokenizer.tokenize()
        self.assertEqual(['(', 'nicht', value_1, ')', 'oder', '(', value_1, 'und', '(', 'nicht', value_2, ')', ')'],
                         token_list)

class FullEvaluationTests(unittest.TestCase):

    def test_sequence_or(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = evaluateTokenList(Tokenizer("A oder B", True, 2, [Aussage(value_a), Aussage(value_b)])
                                           .tokenize()).value
                self.assertEqual(value_a or value_b, result)

    def test_sequence_and(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = evaluateTokenList(Tokenizer("A und B", True, 2, [Aussage(value_a), Aussage(value_b)])
                                           .tokenize()).value
                self.assertEqual(value_a and value_b, result)

    def test_sequence_and_not(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = evaluateTokenList(Tokenizer("A und nicht B", True, 2, [Aussage(value_a), Aussage(value_b)])
                                           .tokenize()).value
                self.assertEqual(value_a and not value_b, result)

    def test_sequence_and_not_not(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = evaluateTokenList(Tokenizer("A und nicht nicht B", True, 2, [Aussage(value_a), Aussage(value_b)])
                                           .tokenize()).value
                self.assertEqual(value_a and not not value_b, result)

    def test_sequence_and_not_not_not(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = evaluateTokenList(Tokenizer("A und nicht nicht nicht B", True, 2, [Aussage(value_a), Aussage(value_b)])
                                           .tokenize()).value
                self.assertEqual(value_a and not not not value_b, result)

if __name__ == '__main__':
    unittest.main()
