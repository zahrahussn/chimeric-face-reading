
### Analysis folder contains R scripts used to produce figures and corresponding analyses
 - figures[2-5]_*_git.R: compute the models for and plot those respective figures, calling on the files in the below folders
 - **eyetracking_preprocessing** folder contains two R scripts used to process individual eyetracking data, resulting in eyedat_clean.csv; all eyetracking preprocessing is in these scripts. Individual data files are available on request.
 - **figures** produced by R scripts are in here
 - **PNG**: files used for image background in figures 3, 4
 - ovalCoordinates.csv: used for some plots

### Data folder contains compiled data files
- biasdat_clean.csv: single-trial bias data
- langdata_clean.csv: language and handedness data
- eyedat_clean.csv: eyetracking + behaviour for 115 eye-tracking subjects

### Materials folder contains the study materials
 - Chimeric Face_Eye Tracker.py is for the experimental task with eyetracking
 - online_Pavlovia: shows the code for the online task (no eyetracking)
 - Final Face Stimuli is called by 1 and includes all face stimuli
