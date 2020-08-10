
#import libraries
from flask import Flask,request,render_template
#tagsearch- contains the function to search for related tags for the given tag from the graph
import tagSearch as ts

#create app
app=Flask(__name__)
# create a page that takes tag input and displays the related tags
@app.route('/')
def recommendation():
        return render_template('recommendation.html')

@app.route('/success',methods=['POST','GET'])
def success():
        tag=request.form["tag"]
        res = ts.find_related_tags(tag)
        return render_template('RelatedTags.html', list_of_tags=res)
#run the app
if __name__=='__main__':
    app.run()
