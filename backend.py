import pathlib
import nltk
import glob
from nltk.sentiment import SentimentIntensityAnalyzer


def get_data(tone):
    dates = []
    score = []
    analyzer = SentimentIntensityAnalyzer()
    filepaths = glob.glob("diary/*.txt")
    for filepath in filepaths:
        filepath = pathlib.Path(filepath)
        date = filepath.stem
        with open(filepath, "r") as file:
            content = file.read()
        scores = analyzer.polarity_scores(content)
        score_tone = scores[tone]
        dates.append(date)
        score.append(score_tone)
    return dates, score


if __name__ == "__main__":
    print(get_data("neg"))





