from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

def index(request):
    return render(request, 'index.html')


def predict_datapoint(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    
    else:
        data=CustomData(

        gender=request.POST.get('gender'),
        race_ethnicity=request.POST.get('ethnicity'),
        parental_level_of_education=request.POST.get('parental_level_of_education'),
        lunch=request.POST.get('lunch'),
        test_preparation_course=request.POST.get('test_preparation_course'),
        reading_score=float(request.POST.get('writing_score')),
        writing_score=float(request.POST.get('reading_score'))

    )
        pred_df=data.get_data_as_data_frame()
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        results = '{:.2f}'.format(results[0])
        
        return render(request, 'home.html', {'results':results})
    