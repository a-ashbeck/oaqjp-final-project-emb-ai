from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

        result_4 = emotion_detector('I am really mad about this')
        self.assertEqual(result_4['label'], 'SENT_NEGATIVE')

        result_5 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_5['label'], 'SENT_NEUTRAL')

unittest.main()