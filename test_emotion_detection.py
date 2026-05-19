from EmotionDetection import emotion_detector

def test_emotions():
    tests = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for text, expected in tests:
        result = emotion_detector(text)
        dominant = result["dominant_emotion"]
        print(f"Testing: {text}")
        print(f"Expected: {expected}, Got: {dominant}")
        assert dominant == expected, f"FAILED: {text}"
        print("PASS\n")

if __name__ == "__main__":
    test_emotions()