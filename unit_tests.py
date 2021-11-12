import unittest
from expression import Expression
from interpreter import Interpreter
from tokenizer import Tokenizer
from view_type import ViewType


class ExpressionTests(unittest.TestCase):

    def test_create_booleans(self):
        tvalue = Expression(True)
        fvalue = Expression(False)
        self.assertTrue(tvalue.value)
        self.assertFalse(fvalue.value)

    def test_create_str_true_false(self):
        tvalue = Expression("true")
        fvalue = Expression("false")
        self.assertTrue(tvalue.value)
        self.assertFalse(fvalue.value)

    def test_create_str_w_f(self):
        tvalue = Expression("w")
        fvalue = Expression("f")
        self.assertTrue(tvalue.value)
        self.assertFalse(fvalue.value)

    def test_create_str_1_0(self):
        tvalue = Expression("1")
        fvalue = Expression("0")
        self.assertTrue(tvalue.value)
        self.assertFalse(fvalue.value)

    def test_string_value_default(self):
        self.test_string_value_binary()

    def test_string_value_binary(self):
        tvalue = Expression(True)
        tvalue.view_type = ViewType.from_str("binär")
        fvalue = Expression(False)
        fvalue.view_type = ViewType.from_str("binär")
        self.assertEqual("1", tvalue.to_str())
        self.assertEqual("0", fvalue.to_str())

    def test_string_value_w_f(self):
        tvalue = Expression(True)
        tvalue.view_type = ViewType.from_str("wf")
        fvalue = Expression(False)
        fvalue.view_type = ViewType.from_str("wf")
        self.assertEqual(tvalue.to_str(), "w")
        self.assertEqual(fvalue.to_str(), "f")

    def test_string_value_true_false(self):
        tvalue = Expression(True)
        tvalue.view_type = ViewType.from_str("truefalse")
        fvalue = Expression(False)
        fvalue.view_type = ViewType.from_str("truefalse")
        self.assertEqual(tvalue.to_str(), "true")
        self.assertEqual(fvalue.to_str(), "false")

    def test_not(self):
        tvalue = Expression(True)
        fvalue = Expression(False)
        self.assertFalse(tvalue.not_().value)
        self.assertTrue(fvalue.not_().value)

    def test_and(self):
        tvalue = Expression(True)
        fvalue = Expression(False)
        self.assertTrue(tvalue.and_(tvalue).value)
        self.assertFalse(tvalue.and_(fvalue).value)
        self.assertFalse(fvalue.and_(tvalue).value)
        self.assertFalse(fvalue.and_(fvalue).value)

    def test_or(self):
        tvalue = Expression(True)
        fvalue = Expression(False)
        self.assertTrue(tvalue.or_(tvalue).value)
        self.assertTrue(tvalue.or_(fvalue).value)
        self.assertTrue(fvalue.or_(tvalue).value)
        self.assertFalse(fvalue.or_(fvalue).value)

    def test_xor(self):
        tvalue = Expression(True)
        fvalue = Expression(False)
        self.assertFalse(tvalue.xor_(tvalue).value)
        self.assertTrue(tvalue.xor_(fvalue).value)
        self.assertTrue(fvalue.xor_(tvalue).value)
        self.assertFalse(fvalue.xor_(fvalue).value)

    def test_implies(self):
        tvalue = Expression(True)
        fvalue = Expression(False)
        self.assertTrue(tvalue.implies_(tvalue).value)
        self.assertFalse(tvalue.implies_(fvalue).value)
        self.assertTrue(fvalue.implies_(tvalue).value)
        self.assertTrue(fvalue.implies_(fvalue).value)


class TokenizerTests(unittest.TestCase):

    def test_sequence_1(self):
        value_1 = Expression(True)
        value_2 = Expression(False)
        tokenizer = Tokenizer("A und nicht B", True, 2, [value_1, value_2])
        token_list = tokenizer.tokenize()
        self.assertEqual([value_1, "und", "(", "nicht", value_2, ")"], token_list)

    def test_sequence_2(self):
        value_1 = Expression(True)
        value_2 = Expression(False)
        tokenizer = Tokenizer("A oder nicht nicht nicht B", True, 2, [value_1, value_2])
        token_list = tokenizer.tokenize()
        self.assertEqual([value_1, "oder", "(", "nicht", value_2, ")"], token_list)

    def test_sequence_3(self):
        value_1 = Expression(True)
        value_2 = Expression(False)
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
                result = Interpreter.evaluate_token_list(Tokenizer("A oder B", True, 2,
                                                                   [Expression(value_a), Expression(value_b)])
                                                         .tokenize()).value
                self.assertEqual(value_a or value_b, result)

    def test_sequence_and(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = Interpreter.evaluate_token_list(Tokenizer("A und B", True, 2,
                                                                   [Expression(value_a), Expression(value_b)])
                                                         .tokenize()).value
                self.assertEqual(value_a and value_b, result)

    def test_sequence_and_not(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = Interpreter.evaluate_token_list(Tokenizer("A und nicht B", True, 2,
                                                                   [Expression(value_a), Expression(value_b)])
                                                         .tokenize()).value
                self.assertEqual(value_a and not value_b, result)

    def test_sequence_and_not_not(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = Interpreter.evaluate_token_list(Tokenizer("A und nicht nicht B", True, 2,
                                                                   [Expression(value_a), Expression(value_b)])
                                                         .tokenize()).value
                self.assertEqual(value_a and not not value_b, result)

    def test_sequence_and_not_not_2(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = Interpreter.evaluate_token_list(Tokenizer("A und nicht nicht (A oder B)", True, 2,
                                                                   [Expression(value_a), Expression(value_b)])
                                                         .tokenize()).value
                self.assertEqual(value_a and not not (value_a or value_b), result)

    def test_sequence_or_not_not(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = Interpreter.evaluate_token_list(Tokenizer("A oder nicht nicht (A oder B)", True, 2,
                                                                   [Expression(value_a), Expression(value_b)])
                                                         .tokenize()).value
                self.assertEqual(value_a or not not (value_a or value_b), result)

    def test_sequence_and_not_not_not(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = Interpreter.evaluate_token_list(Tokenizer("A und nicht nicht nicht B", True, 2,
                                                                   [Expression(value_a), Expression(value_b)])
                                                         .tokenize()).value
                self.assertEqual(value_a and not not not value_b, result)

    def test_sequence_and_not_not_not_2(self):
        list_a = [True, False]
        list_b = [True, False]
        for value_a in list_a:
            for value_b in list_b:
                result = Interpreter.evaluate_token_list(Tokenizer("A und (nicht (nicht (nicht B)))", True, 2,
                                                                   [Expression(value_a), Expression(value_b)])
                                                         .tokenize()).value
                self.assertEqual(value_a and not not not value_b, result)


if __name__ == '__main__':
    unittest.main()
