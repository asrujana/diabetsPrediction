


app = Flask(__name__ , template_folder='template')
model = pickle.load(open('model.pkl','rb'))
