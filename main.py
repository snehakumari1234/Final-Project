1.a) import pandas as pd
      df= pd.red.csv
      print (df.head ()) 
  b) checking for missing values--
     missing values= df.isnull().sum() 
     print ("Missing values in each column: ") 
     print (missing_values) 
  c) Converting categories columns using label encoding--
     from sklearn.preprocessing import LabelEncoder
     df ['Category_column']= label_encoder.fit_transform (df['Category_column']) 
     print (df.head()) 

2. a) import pandas as pd
      import matplotlib.pyplot as plt
      df= pd.read.csv
      plt.figure(figsize=(10,6)) 
      plt.hist (df['score_column'], bins=20, color='blue', alpha=0.7, edgecolor='black') 
      plt.title ('score Distribution') 
      plt.xlabel('scores') 
      plt.ylabel('Frequency') 
      plt.grib (axis='y', alpha=0.75) 
      plt.show() 

   b) import pandas as pd
      df= pd.read.csv
      average_scores_gender= df.groupby('gender') ['math score', 'reading score', 'writing score'].mean() 
      average_scores_lunch= df.groupby ('lunch') ['math score', 'reading score', 'writing score'].mean() 
      average_scores_test_prep= df.groupby('test preparation course') ['math score', 'reading score', 'writing score'].mean() 

      print("Average scores by Gender: ") 
      print(average_scores_gender) 

      print("\n Average scores by Lunch Type: ") 
      print(average_scores_lunch) 

      print("\n Average scores by Test preparation status: ") 
      print(average_scores_test_prep) 

    c) import pandas as pd
       import seaborn as sns  
       import matplotlib.pyplot as plt
       df= pd.read.csv ('student_performance.csv') 

       df_encoded= pd.get_dummies (df, columns=['gender', 'lunch', 'test preparation course'], drop_first=True) 

       numeric_cols= df_encoded.select_dtypes(include= ['int64', 'float64']) 

       corr_matix= df_numeric.corr() 

       plt. figure(figsize= (12, 8)) 
       sns.heatmap (corr_matrix, 
                    annot=True, 
                    cmap='coolwarm', 
                    center=0, 
                    fmt= '. 2f', 
                    linewidths=0.5, 
                    annot_kws={'size':10}) 
      plt.title ('Student Performance Correlation Heatmap', pad=20, frontsize=16) 
      plt. xticks(rotation=45, ha='right') 
      plt. yticks(rotation=0)  
      plt. tight_layout () 
      plt. show() 

3. a) import pandas as pd
      df= pd.read.csv
      df['average_score']= df[['math score', 'reading score', 'writing score']].mean(axis=1) 

      print(df.head()) 

   c) import pandas as pd    
      import numpy as np  
      df= pd. read. csv

      df['result_binary']= np.where (df['average_score']>=50, 1,0) 

      print(df[['average_score', 'result_binary']].head()) 

      
