from flask import Flask, render_template, request
from Stopwordremover import StopWordRemover
from tokanized import Tokenizer
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['area']
      word = Tokenizer(result)
      short = word.word_tokenize()
      stop_words = set(StopWordRemover.get_stopwords(""))
      filter_sentences=[]
      for w in short:
        if w not in stop_words:
            filter_sentences.append(w)
      return render_template("result.html",result = short,filter = filter_sentences)
   else:
      return render_template('student.html')

if __name__ == '__main__':
   app.run(debug = True)

