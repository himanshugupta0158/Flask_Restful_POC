from flask import Flask , request 
from flask_restful import Resource , Api , reqparse , abort , fields , marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    views = db.Column(db.Integer , nullable=False)
    likes = db.Column(db.Integer , nullable=False)
    
    def __repr__(self):
        return f"Video(name = {self.name} , views = {self.views}, likes = {self.likes})"

# db.create_all()



video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str , help="Name of the video is required" , required=True)
video_put_args.add_argument("views", type=int , help="views of the video is required" , required=True)
video_put_args.add_argument("likes", type=int , help="likes on the video is required" , required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str , help="Name of the video is required" )
video_update_args.add_argument("views", type=int , help="views of the video is required")
video_update_args.add_argument("likes", type=int , help="likes on the video is required")

resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer
}



class Video(Resource):
    
    @marshal_with(resource_fields)
    def get(self , video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result :
            abort(404, message="Could not find video with that id...")
        return result
    
    @marshal_with(resource_fields)
    def post(self , video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result :
            abort(409,message="Video id is already taken...")
        video = VideoModel(id=video_id,name=args['name'],views=args['views'],likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video , 201
    
    @marshal_with(resource_fields)
    def put(self , video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result :
            abort(404,message="Video does't exist, cannot update")
        if args['name'] and args['views'] and args['likes'] :
            result.name = args['name']
            result.views = args['views']
            result.likes = args['likes']
        else:
            abort(403 , message="name,views and likes all fields should be given")
        
        db.session.commit()
        
        return result
     

    @marshal_with(resource_fields)
    def patch(self , video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result :
            abort(404,message="Video does't exist, cannot update")
        if args['name'] :
            result.name = args['name']
        if args['views'] :
            result.views = args['views']
        if args['likes'] :
            result.likes = args['likes']
        
        db.session.commit()
        return result
    
    def delete(self ,video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result :
            abort(404, message="Could not find video with that id...")
        db.session.delete(result)
        db.session.commit()
        msg = f"video id {video_id} is deleted successfully."
        return {"Deleted" : msg }, 200

class AllVideos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = VideoModel.query.all()
        if not result :
            abort(404, message="there is no video in db...")
        return result
        
    
api.add_resource(Video , "/video/<int:video_id>")
api.add_resource(AllVideos , "/allvideos")


if __name__ == '__main__':
    app.run(debug=True)
# debug=True means it will show all the logs and errors occur there.




"""
# this is practice api
names = {'jake':{'age':21 , 'gender':'male'},
        'kale':{'age':18 , 'gender':'female'}
        }


class HelloWorld(Resource):
    def get(self , name ):
        return names[name]
    
    # def post(self):
    #     return {'data':'posted'}
    
api.add_resource(HelloWorld, '/helloworld/<string:name>')
"""
