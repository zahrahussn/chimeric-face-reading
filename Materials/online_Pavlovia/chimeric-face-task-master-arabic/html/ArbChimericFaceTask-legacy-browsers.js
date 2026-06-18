/**************************** 
 * Arbchimericfacetask Test *
 ****************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'ArbChimericFaceTask';  // from the Builder filename that created this script
let expInfo = {'أول حرف من الاسم و الشهرة': '', 'العمر': '', 'الجنس': '', 'بلد الإقامة': '', 'اللغة الأم': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const consentFormLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(consentFormLoopLoopBegin, consentFormLoopLoopScheduler);
flowScheduler.add(consentFormLoopLoopScheduler);
flowScheduler.add(consentFormLoopLoopEnd);
flowScheduler.add(AcceptConsentRoutineBegin());
flowScheduler.add(AcceptConsentRoutineEachFrame());
flowScheduler.add(AcceptConsentRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(QstartRoutineBegin());
flowScheduler.add(QstartRoutineEachFrame());
flowScheduler.add(QstartRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(LanguagesRoutineBegin());
flowScheduler.add(LanguagesRoutineEachFrame());
flowScheduler.add(LanguagesRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(ProficiencyEngRoutineBegin());
flowScheduler.add(ProficiencyEngRoutineEachFrame());
flowScheduler.add(ProficiencyEngRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(ActivitiesEngRoutineBegin());
flowScheduler.add(ActivitiesEngRoutineEachFrame());
flowScheduler.add(ActivitiesEngRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(ReadingEngRoutineBegin());
flowScheduler.add(ReadingEngRoutineEachFrame());
flowScheduler.add(ReadingEngRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(ProficiencyArRoutineBegin());
flowScheduler.add(ProficiencyArRoutineEachFrame());
flowScheduler.add(ProficiencyArRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(ActivitiesArRoutineBegin());
flowScheduler.add(ActivitiesArRoutineEachFrame());
flowScheduler.add(ActivitiesArRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(ReadingArRoutineBegin());
flowScheduler.add(ReadingArRoutineEachFrame());
flowScheduler.add(ReadingArRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(TimeArRoutineBegin());
flowScheduler.add(TimeArRoutineEachFrame());
flowScheduler.add(TimeArRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(HandednessRoutineBegin());
flowScheduler.add(HandednessRoutineEachFrame());
flowScheduler.add(HandednessRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(Q_FinishRoutineBegin());
flowScheduler.add(Q_FinishRoutineEachFrame());
flowScheduler.add(Q_FinishRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(PracticeInstrRoutineBegin());
flowScheduler.add(PracticeInstrRoutineEachFrame());
flowScheduler.add(PracticeInstrRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
const trialsPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeLoopBegin, trialsPracticeLoopScheduler);
flowScheduler.add(trialsPracticeLoopScheduler);
flowScheduler.add(trialsPracticeLoopEnd);
flowScheduler.add(TrialsInstrRoutineBegin());
flowScheduler.add(TrialsInstrRoutineEachFrame());
flowScheduler.add(TrialsInstrRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
const trialsChimericLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsChimericLoopBegin, trialsChimericLoopScheduler);
flowScheduler.add(trialsChimericLoopScheduler);
flowScheduler.add(trialsChimericLoopEnd);
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var ConsentFormClock;
var consentForm;
var spaceConsent;
var key_resp;
var Blank500Clock;
var textBlank;
var AcceptConsentClock;
var text;
var key_resp_2;
var QstartClock;
var key_resp_3;
var text_2;
var text_3;
var text_4;
var text_5;
var LanguagesClock;
var InstrLanguages;
var InstrLang2;
var InstrLang3;
var InstrLang4;
var InstrLang5;
var InstrLang6;
var InstrLang7;
var fluentLang;
var spaceTextLang;
var ProficiencyEngClock;
var textProficiencyEng;
var MouseInstruction;
var engSpeak;
var engRead;
var engWrite;
var eSpeakLabel;
var eReadLabel;
var eWriteLabel;
var spaceText;
var spaceKey;
var mouseProf;
var ActivitiesEngClock;
var textActivitiesEng;
var text_6;
var engSpeakFreq;
var engListenFreq;
var engReadFreq;
var engWriteFreq;
var engSpeakLabel;
var engListenLabel;
var engReadLabel;
var engWriteLabel;
var textSpaceActivitiesEng;
var keyActivitiesEng;
var mouseActEng;
var ReadingEngClock;
var hoursReading;
var text_8;
var slider_engReadHrs;
var space;
var key_reading;
var ProficiencyArClock;
var textProficiencyArb;
var text_7;
var ArSpeak;
var ArRead;
var ArWrite;
var arSpeakLabel;
var arReadLabel;
var arWriteLabel;
var textSpaceAr;
var keySpaceAr;
var ActivitiesArClock;
var textActivitiesAr;
var text_9;
var arSpeakFreq;
var arListenFreq;
var arReadFreq;
var arWriteFreq;
var aSpeakLabel;
var aListenLabel;
var aReadLabel;
var aWriteLabel;
var textSpaceActivitiesAr;
var keySpaceActivitiesAr;
var ReadingArClock;
var readingAr;
var text_10;
var spaceContinue_3;
var key_space;
var arReadHrs;
var TimeArClock;
var textLongCountAr;
var spaceContinue_2;
var Option1;
var Option2;
var Option3;
var Option4;
var Option5;
var arbCountryTime;
var key_space_3;
var HandednessClock;
var textHandedness;
var writeHand;
var throwHand;
var toothHand;
var spoonHand;
var writeHandLabel;
var throwHandLabel;
var toothHandLabel;
var spoonHandLabel;
var textSpaceHand;
var keySpaceHand;
var Q_FinishClock;
var QDone;
var text_11;
var finishQKey;
var PracticeInstrClock;
var practiceInstr;
var textSpacePractInstr;
var practiceInst2;
var practiceInstr3;
var practiceInstr4;
var practiceInstr5;
var SpacePracticInst;
var mouse;
var PracticeTrialsClock;
var imageCenterPract;
var imageLVFPract;
var imageRVFPract;
var keyChimericPract;
var imageCentLabel;
var imageLVFLabel;
var imageRVFLabel;
var TrialsInstrClock;
var trialsInstr1;
var trialsInstr2;
var trialsInstr3;
var trialsInstr4;
var trialsInstr5;
var textSpaceTrials;
var keySpaceTrialsInstr;
var ChimericTrialsClock;
var imageCenter;
var imageLVF;
var imageRVF;
var keyChimeric;
var EndScreenClock;
var End;
var keyEnd;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "ConsentForm"
  ConsentFormClock = new util.Clock();
  consentForm = new visual.ImageStim({
    win : psychoJS.window,
    name : 'consentForm', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.7, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  spaceConsent = new visual.TextStim({
    win: psychoJS.window,
    name: 'spaceConsent',
    text: 'الرجاء قراءة استمارة الموافقة \nو الضغط على شريط المسافة\n للمتابعة (space bar)',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "AcceptConsent"
  AcceptConsentClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'إذا قرأت المعلومات المذكورة أعلاه ووافقت عليها\n\n يرجى الضغط على شريط المسافة للبدء بالدراسة \n',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Qstart"
  QstartClock = new util.Clock();
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'أولاً، سوف نطرح عليك بعض الأسئلة حول معرفتك اللغوية    ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.04,  wrapWidth: 1, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -1.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'و بعد ذلك، ستقوم بالمهمة التجريبية',
    font: 'Arial',
    units: undefined, 
    pos: [0.03, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'ستستغرق التجربة بأكملها حوالي\xa0 30 دقيقة',
    font: 'Arial',
    units: undefined, 
    pos: [0.01, (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'اضغط على شريط المسافة للمتابعة',
    font: 'Arial',
    units: undefined, 
    pos: [0.02, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Languages"
  LanguagesClock = new util.Clock();
  InstrLanguages = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrLanguages',
    text: 'ما هي اللغة التي تعرفها بطلاقة أكثر من أي لغة أخرى؟',
    font: 'Arial',
    units: undefined, 
    pos: [0.16, 0.3], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  InstrLang2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrLang2',
    text: '١. الإنجليزية أو الفرنسية أو لغة أوروبية أخرى\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.15, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  InstrLang3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrLang3',
    text: '٢. العربية، العبرية، الأردية، الفارسية، الآرامية، الآذرية أو الكردية\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.02, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  InstrLang4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrLang4',
    text: '٣. الهندية أو الملايو أو غيرها من لغات جنوب آسيا أو جنوب شرق آسيا\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  InstrLang5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrLang5',
    text: '٤. الصينية أو اليابانية أو الكورية\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.25, (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  InstrLang6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrLang6',
    text: '٥. الأمهرية أو البربرية أو غيرها من اللغات الأفريقية\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.11, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  InstrLang7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrLang7',
    text: '٦. أخرى\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  fluentLang = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  spaceTextLang = new visual.TextStim({
    win: psychoJS.window,
    name: 'spaceTextLang',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ProficiencyEng"
  ProficiencyEngClock = new util.Clock();
  textProficiencyEng = new visual.TextStim({
    win: psychoJS.window,
    name: 'textProficiencyEng',
    text: 'ما مدى إتقانك للغة الإنجليزية أو أي لغة مكتوبة من اليسار إلى اليمين؟\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.32], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  MouseInstruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'MouseInstruction',
    text: '\nاستخدم الماوس للرد على هذه الأسئلة\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.18, 0.28], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  engSpeak = new visual.Slider({
    win: psychoJS.window, name: 'engSpeak',
    size: [0.5, 0.02], pos: [0, 0.2], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  engRead = new visual.Slider({
    win: psychoJS.window, name: 'engRead',
    size: [0.5, 0.02], pos: [0, 0], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  engWrite = new visual.Slider({
    win: psychoJS.window, name: 'engWrite',
    size: [0.5, 0.02], pos: [0, (- 0.2)], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  eSpeakLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'eSpeakLabel',
    text: 'التكلم',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  eReadLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'eReadLabel',
    text: 'القراءة',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  eWriteLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'eWriteLabel',
    text: 'الكتابة',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  spaceText = new visual.TextStim({
    win: psychoJS.window,
    name: 'spaceText',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  spaceKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouseProf = new core.Mouse({
    win: psychoJS.window,
  });
  mouseProf.mouseClock = new util.Clock();
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ActivitiesEng"
  ActivitiesEngClock = new util.Clock();
  textActivitiesEng = new visual.TextStim({
    win: psychoJS.window,
    name: 'textActivitiesEng',
    text: 'إلى أي مدى تستخدم اللغة الإنجليزية أو لغة مكتوبة من اليسار إلى اليمين أثناء؟\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.32], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'استخدم الماوس للرد على هذه الأسئلة  ',
    font: 'Arial',
    units: undefined, 
    pos: [0.18, 0.26], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  engSpeakFreq = new visual.Slider({
    win: psychoJS.window, name: 'engSpeakFreq',
    size: [0.5, 0.02], pos: [0, 0.2], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  engListenFreq = new visual.Slider({
    win: psychoJS.window, name: 'engListenFreq',
    size: [0.5, 0.02], pos: [0, 0.08], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  engReadFreq = new visual.Slider({
    win: psychoJS.window, name: 'engReadFreq',
    size: [0.5, 0.02], pos: [0, (- 0.04)], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  engWriteFreq = new visual.Slider({
    win: psychoJS.window, name: 'engWriteFreq',
    size: [0.5, 0.02], pos: [0, (- 0.16)], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  engSpeakLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'engSpeakLabel',
    text: 'التكلم',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  engListenLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'engListenLabel',
    text: 'الإصغاء\n',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, 0.08], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  engReadLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'engReadLabel',
    text: 'القراءة',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, (- 0.04)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  engWriteLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'engWriteLabel',
    text: 'الكتابة',
    font: 'Arial',
    units: undefined, 
    pos: [0.35, (- 0.16)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  textSpaceActivitiesEng = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceActivitiesEng',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -10.0 
  });
  
  keyActivitiesEng = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouseActEng = new core.Mouse({
    win: psychoJS.window,
  });
  mouseActEng.mouseClock = new util.Clock();
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ReadingEng"
  ReadingEngClock = new util.Clock();
  hoursReading = new visual.TextStim({
    win: psychoJS.window,
    name: 'hoursReading',
    text: 'كم ساعة في اليوم تقضيها في قراءة مواد (إما مطبوعة أو على الإنترنت) باللغة الإنجليزية أو لغة مكتوبة من اليسار إلى اليمين؟',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'استخدم الماوس للرد على هذه الأسئلة  ',
    font: 'Arial',
    units: undefined, 
    pos: [0.37, 0.25], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  slider_engReadHrs = new visual.Slider({
    win: psychoJS.window, name: 'slider_engReadHrs',
    size: [0.5, 0.02], pos: [0, 0.15], units: 'height',
    labels: ['8+', '8-6', '6-4', '4-2', '<2'], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  space = new visual.TextStim({
    win: psychoJS.window,
    name: 'space',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  key_reading = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ProficiencyAr"
  ProficiencyArClock = new util.Clock();
  textProficiencyArb = new visual.TextStim({
    win: psychoJS.window,
    name: 'textProficiencyArb',
    text: 'ما مدى إتقانك للغة العربية أو العبرية أو الأردية أو أي لغة مكتوبة من اليمين إلى اليسار؟',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.32], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'استخدم الماوس للرد على هذه الأسئلة  ',
    font: 'Arial',
    units: undefined, 
    pos: [0.22, 0.26], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  ArSpeak = new visual.Slider({
    win: psychoJS.window, name: 'ArSpeak',
    size: [0.5, 0.02], pos: [0, 0.2], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  ArRead = new visual.Slider({
    win: psychoJS.window, name: 'ArRead',
    size: [0.5, 0.02], pos: [0, 0], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  ArWrite = new visual.Slider({
    win: psychoJS.window, name: 'ArWrite',
    size: [0.5, 0.02], pos: [0, (- 0.2)], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  arSpeakLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'arSpeakLabel',
    text: 'التكلم',
    font: 'Arial',
    units: undefined, 
    pos: [0.35, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  arReadLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'arReadLabel',
    text: 'القراءة',
    font: 'Arial',
    units: undefined, 
    pos: [0.35, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  arWriteLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'arWriteLabel',
    text: 'الكتابة',
    font: 'Arial',
    units: undefined, 
    pos: [0.35, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  textSpaceAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceAr',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  keySpaceAr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ActivitiesAr"
  ActivitiesArClock = new util.Clock();
  textActivitiesAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textActivitiesAr',
    text: 'إلى أي مدى تستخدم اللغة العربية أو لغة مكتوبة من اليمين إلى اليسار أثناء؟\n',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.32], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'استخدم الماوس للرد على هذه الأسئلة',
    font: 'Arial',
    units: undefined, 
    pos: [0.18, 0.26], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  arSpeakFreq = new visual.Slider({
    win: psychoJS.window, name: 'arSpeakFreq',
    size: [0.5, 0.02], pos: [0, 0.2], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  arListenFreq = new visual.Slider({
    win: psychoJS.window, name: 'arListenFreq',
    size: [0.5, 0.02], pos: [0, 0.08], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  arReadFreq = new visual.Slider({
    win: psychoJS.window, name: 'arReadFreq',
    size: [0.5, 0.02], pos: [0, (- 0.04)], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  arWriteFreq = new visual.Slider({
    win: psychoJS.window, name: 'arWriteFreq',
    size: [0.5, 0.02], pos: [0, (- 0.16)], units: 'height',
    labels: [4, '', 2, '', 0], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  aSpeakLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'aSpeakLabel',
    text: 'التكلم',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  aListenLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'aListenLabel',
    text: 'الإصغاء\n',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, 0.08], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  aReadLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'aReadLabel',
    text: 'القراءة',
    font: 'Arial',
    units: 'height', 
    pos: [0.35, (- 0.04)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  aWriteLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'aWriteLabel',
    text: 'الكتابة',
    font: 'Arial',
    units: undefined, 
    pos: [0.35, (- 0.16)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  textSpaceActivitiesAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceActivitiesAr',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -10.0 
  });
  
  keySpaceActivitiesAr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ReadingAr"
  ReadingArClock = new util.Clock();
  readingAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'readingAr',
    text: 'كم ساعة في اليوم  تقضيها في قراءة مواد (إما مطبوعة أو على الإنترنت) باللغة العربية أو لغة مكتوبة من اليمين إلى اليسار؟',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.3], height: 0.04,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'استخدم الماوس للرد على هذه الأسئلة',
    font: 'Arial',
    units: undefined, 
    pos: [0.37, 0.25], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  spaceContinue_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'spaceContinue_3',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  key_space = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  arReadHrs = new visual.Slider({
    win: psychoJS.window, name: 'arReadHrs',
    size: [0.5, 0.02], pos: [0, 0.15], units: 'height',
    labels: ['8+', '8-6', '6-4', '4-2', '<2'], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('White'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TimeAr"
  TimeArClock = new util.Clock();
  textLongCountAr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textLongCountAr',
    text: 'ما المدة التي عشت خلالها في بلد حيث اللغة العربية أو العبرية أو الأردية أو الفارسية أو الآرامية هي اللغة السائدة للتواصل؟',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.32], height: 0.04,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  spaceContinue_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'spaceContinue_2',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  Option1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Option1',
    text: '١.صفر سنوات\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  Option2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Option2',
    text: '٢.أقل من سنة واحدة\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.02, 0.15], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  Option3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Option3',
    text: '٣. بين ٢-٣ سنوات\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.02, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  Option4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Option4',
    text: '٤. بين ٤-٧ سنوات\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.02, 0.05], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  Option5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Option5',
    text: '٥. أكثر من ٧ سنوات\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.02, 0.0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  arbCountryTime = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_space_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Handedness"
  HandednessClock = new util.Clock();
  textHandedness = new visual.TextStim({
    win: psychoJS.window,
    name: 'textHandedness',
    text: 'يرجى الاشارة إلى أي يد تفضل استخدام أثناء\n\nاستخدم الماوس للرد على هذه الأسئلة',
    font: 'Arial',
    units: undefined, 
    pos: [0.03, 0.3], height: 0.04,  wrapWidth: 27, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  writeHand = new visual.Slider({
    win: psychoJS.window, name: 'writeHand',
    size: [0.8, 0.02], pos: [(- 0.2), 0.2], units: 'height',
    labels: ['اليمين دائما', 'اليمين عادة', 'كلاهما بالتساوي', 'اليسار عادة', 'اليسار دائما'], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('white'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  throwHand = new visual.Slider({
    win: psychoJS.window, name: 'throwHand',
    size: [0.8, 0.02], pos: [(- 0.2), 0.08], units: 'height',
    labels: ['اليمين دائما', 'اليمين عادة', 'كلاهما بالتساوي', 'اليسار عادة', 'اليسار دائما'], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('white'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  toothHand = new visual.Slider({
    win: psychoJS.window, name: 'toothHand',
    size: [0.8, 0.02], pos: [(- 0.2), (- 0.04)], units: 'height',
    labels: ['اليمين دائما', 'اليمين عادة', 'كلاهما بالتساوي', 'اليسار عادة', 'اليسار دائما'], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('white'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  spoonHand = new visual.Slider({
    win: psychoJS.window, name: 'spoonHand',
    size: [0.8, 0.02], pos: [(- 0.2), (- 0.16)], units: 'height',
    labels: ['اليمين دائما', 'اليمين عادة', 'كلاهما بالتساوي', 'اليسار عادة', 'اليسار دائما'], ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('white'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  writeHandLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'writeHandLabel',
    text: 'القراءة',
    font: 'Arial',
    units: 'height', 
    pos: [0.4, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  throwHandLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'throwHandLabel',
    text: 'الرمي\n',
    font: 'Arial',
    units: 'height', 
    pos: [0.4, 0.08], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  toothHandLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'toothHandLabel',
    text: 'استخدام فرشاة الأسنان',
    font: 'Arial',
    units: 'height', 
    pos: [0.43, (- 0.04)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  spoonHandLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'spoonHandLabel',
    text: 'استخدام الملعقة',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.16)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  textSpaceHand = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceHand',
    text: 'اضغط على شريط المسافة للمتابعة ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: 27, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -9.0 
  });
  
  keySpaceHand = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Q_Finish"
  Q_FinishClock = new util.Clock();
  QDone = new visual.TextStim({
    win: psychoJS.window,
    name: 'QDone',
    text: ' اكتمل الاستبيان\n',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: 0.0 
  });
  
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: 'اضغط على شريط المسافة لمتابعة التجربة \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  finishQKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PracticeInstr"
  PracticeInstrClock = new util.Clock();
  practiceInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceInstr',
    text: 'في هذه المهمة، ستحدد مدى تشابه الوجوه. سيظهر لك ٣ وجوه على الشاشة في كل محاولة. الوجه في وسط الشاشة هو الهدف\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.0, 0.3], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: 0.0 
  });
  
  textSpacePractInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpacePractInstr',
    text: 'اضغط على شريط المسافة للمتابعة',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -1.0 
  });
  
  practiceInst2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceInst2',
    text: '\nاضغط على السهم الأيسر على لوحة المفاتيح إذا كان الوجه الموجود على اليسار يشبه أكثر الوجه الموجود في وسط الشاشة \n',
    font: 'Arial',
    units: undefined, 
    pos: [0.03, 0.2], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  practiceInstr3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceInstr3',
    text: ' إذا كان الوجه الموجود على اليمين يبدو أكثر مثل الوجه الموجود في وسط الشاشة فاضغط على السهم الأيمن على لوحة المفاتيح',
    font: 'Arial',
    units: undefined, 
    pos: [0.03, 0.1], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  practiceInstr4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceInstr4',
    text: 'ليس هناك جواب صحيح أو خاطئ. في بعض الأحيان، قد يكون من الصعب اتخاذ قرار، هذا أمر طبيعي تماما\n',
    font: 'Arial',
    units: undefined, 
    pos: [0.03, (- 0.05)], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  practiceInstr5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceInstr5',
    text: 'ستبدأ أولا ببعض المحاولات التدريبية تليها التجربة الرئيسية',
    font: 'Arial',
    units: undefined, 
    pos: [0.03, (- 0.15)], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  SpacePracticInst = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  mouse.setVisible(false);
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PracticeTrials"
  PracticeTrialsClock = new util.Clock();
  imageCenterPract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageCenterPract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  imageLVFPract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageLVFPract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  imageRVFPract = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageRVFPract', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  keyChimericPract = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imageCentLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'imageCentLabel',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -4.0 
  });
  
  imageLVFLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'imageLVFLabel',
    text: 'اضغط على مفتاح السهم الأيسر\nإذا كنت تعتقد أن هذا الوجه\nيبدو أكثر مثل الهدف\n',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.45), (- 0.2)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -5.0 
  });
  
  imageRVFLabel = new visual.TextStim({
    win: psychoJS.window,
    name: 'imageRVFLabel',
    text: 'اضغط على مفتاح السهم الأيمن\nإذا كنت تعتقد أن هذا الوجه\nيبدو أكثر مثل الهدف',
    font: 'Arial',
    units: undefined, 
    pos: [0.45, (- 0.2)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('Black'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TrialsInstr"
  TrialsInstrClock = new util.Clock();
  trialsInstr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialsInstr1',
    text: 'ستبدأ الآن التجربة الفعلية',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: 1, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  trialsInstr2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialsInstr2',
    text: 'الوجه في الوسط هو الوجه الهدف',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  trialsInstr3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialsInstr3',
    text: ' إذا كان الوجه الموجود على اليسار يشبه أكثر الوجه في الوسط فاضغط على السهم الأيسر',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  trialsInstr4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialsInstr4',
    text: 'اضغط على السهم الأيمن إذا كان الوجه الموجود على اليمين يشبه أكثر الوجه في الوسط',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.0], height: 0.04,  wrapWidth: 2, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  trialsInstr5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialsInstr5',
    text: '\nليس هناك جواب صحيح أو خاطئ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  textSpaceTrials = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpaceTrials',
    text: 'اضغط على شريط المسافة للمتابعة',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  keySpaceTrialsInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ChimericTrials"
  ChimericTrialsClock = new util.Clock();
  imageCenter = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageCenter', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  imageLVF = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageLVF', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  imageRVF = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageRVF', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.26,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  keyChimeric = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  End = new visual.TextStim({
    win: psychoJS.window,
    name: 'End',
    text: 'شكرا لك على مشاركتك في هذه الدراسة\n\nاضغط على مفتاح الهروب  للخروج \n(esc)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  keyEnd = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var consentFormLoop;
var currentLoop;
function consentFormLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  consentFormLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'consentForm.xlsx',
    seed: undefined, name: 'consentFormLoop'
  });
  psychoJS.experiment.addLoop(consentFormLoop); // add the loop to the experiment
  currentLoop = consentFormLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  consentFormLoop.forEach(function() {
    const snapshot = consentFormLoop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(ConsentFormRoutineBegin(snapshot));
    thisScheduler.add(ConsentFormRoutineEachFrame(snapshot));
    thisScheduler.add(ConsentFormRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function consentFormLoopLoopEnd() {
  psychoJS.experiment.removeLoop(consentFormLoop);

  return Scheduler.Event.NEXT;
}


var trialsPractice;
function trialsPracticeLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsPractice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'PracticeStimuliPavlovia.xlsx',
    seed: undefined, name: 'trialsPractice'
  });
  psychoJS.experiment.addLoop(trialsPractice); // add the loop to the experiment
  currentLoop = trialsPractice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialsPractice.forEach(function() {
    const snapshot = trialsPractice.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(PracticeTrialsRoutineBegin(snapshot));
    thisScheduler.add(PracticeTrialsRoutineEachFrame(snapshot));
    thisScheduler.add(PracticeTrialsRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsPracticeLoopEnd() {
  psychoJS.experiment.removeLoop(trialsPractice);

  return Scheduler.Event.NEXT;
}


var trialsChimeric;
function trialsChimericLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsChimeric = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'ImageStimuliPavlovia.xlsx',
    seed: undefined, name: 'trialsChimeric'
  });
  psychoJS.experiment.addLoop(trialsChimeric); // add the loop to the experiment
  currentLoop = trialsChimeric;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialsChimeric.forEach(function() {
    const snapshot = trialsChimeric.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(ChimericTrialsRoutineBegin(snapshot));
    thisScheduler.add(ChimericTrialsRoutineEachFrame(snapshot));
    thisScheduler.add(ChimericTrialsRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsChimericLoopEnd() {
  psychoJS.experiment.removeLoop(trialsChimeric);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_allKeys;
var ConsentFormComponents;
function ConsentFormRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ConsentForm'-------
    t = 0;
    ConsentFormClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    consentForm.setImage(image);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    ConsentFormComponents = [];
    ConsentFormComponents.push(consentForm);
    ConsentFormComponents.push(spaceConsent);
    ConsentFormComponents.push(key_resp);
    
    ConsentFormComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function ConsentFormRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ConsentForm'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ConsentFormClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consentForm* updates
    if (t >= 0.0 && consentForm.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentForm.tStart = t;  // (not accounting for frame time here)
      consentForm.frameNStart = frameN;  // exact frame index
      
      consentForm.setAutoDraw(true);
    }

    
    // *spaceConsent* updates
    if (t >= 0.0 && spaceConsent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      spaceConsent.tStart = t;  // (not accounting for frame time here)
      spaceConsent.frameNStart = frameN;  // exact frame index
      
      spaceConsent.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 1.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ConsentFormComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ConsentFormRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ConsentForm'-------
    ConsentFormComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "ConsentForm" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Blank500Components;
function Blank500RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Blank500'-------
    t = 0;
    Blank500Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Blank500Components = [];
    Blank500Components.push(textBlank);
    
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function Blank500RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Blank500'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textBlank* updates
    if (t >= 0.0 && textBlank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textBlank.tStart = t;  // (not accounting for frame time here)
      textBlank.frameNStart = frameN;  // exact frame index
      
      textBlank.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textBlank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textBlank.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Blank500RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Blank500'-------
    Blank500Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var AcceptConsentComponents;
function AcceptConsentRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'AcceptConsent'-------
    t = 0;
    AcceptConsentClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    AcceptConsentComponents = [];
    AcceptConsentComponents.push(text);
    AcceptConsentComponents.push(key_resp_2);
    
    AcceptConsentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function AcceptConsentRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'AcceptConsent'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = AcceptConsentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AcceptConsentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AcceptConsentRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'AcceptConsent'-------
    AcceptConsentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "AcceptConsent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var QstartComponents;
function QstartRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Qstart'-------
    t = 0;
    QstartClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    QstartComponents = [];
    QstartComponents.push(key_resp_3);
    QstartComponents.push(text_2);
    QstartComponents.push(text_3);
    QstartComponents.push(text_4);
    QstartComponents.push(text_5);
    
    QstartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function QstartRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Qstart'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = QstartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    QstartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function QstartRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Qstart'-------
    QstartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "Qstart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fluentLang_allKeys;
var LanguagesComponents;
function LanguagesRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Languages'-------
    t = 0;
    LanguagesClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    fluentLang.keys = undefined;
    fluentLang.rt = undefined;
    _fluentLang_allKeys = [];
    // keep track of which components have finished
    LanguagesComponents = [];
    LanguagesComponents.push(InstrLanguages);
    LanguagesComponents.push(InstrLang2);
    LanguagesComponents.push(InstrLang3);
    LanguagesComponents.push(InstrLang4);
    LanguagesComponents.push(InstrLang5);
    LanguagesComponents.push(InstrLang6);
    LanguagesComponents.push(InstrLang7);
    LanguagesComponents.push(fluentLang);
    LanguagesComponents.push(spaceTextLang);
    
    LanguagesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function LanguagesRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Languages'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = LanguagesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstrLanguages* updates
    if (t >= 0.0 && InstrLanguages.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrLanguages.tStart = t;  // (not accounting for frame time here)
      InstrLanguages.frameNStart = frameN;  // exact frame index
      
      InstrLanguages.setAutoDraw(true);
    }

    
    // *InstrLang2* updates
    if (t >= 0.0 && InstrLang2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrLang2.tStart = t;  // (not accounting for frame time here)
      InstrLang2.frameNStart = frameN;  // exact frame index
      
      InstrLang2.setAutoDraw(true);
    }

    
    // *InstrLang3* updates
    if (t >= 0.0 && InstrLang3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrLang3.tStart = t;  // (not accounting for frame time here)
      InstrLang3.frameNStart = frameN;  // exact frame index
      
      InstrLang3.setAutoDraw(true);
    }

    
    // *InstrLang4* updates
    if (t >= 0.0 && InstrLang4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrLang4.tStart = t;  // (not accounting for frame time here)
      InstrLang4.frameNStart = frameN;  // exact frame index
      
      InstrLang4.setAutoDraw(true);
    }

    
    // *InstrLang5* updates
    if (t >= 0.0 && InstrLang5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrLang5.tStart = t;  // (not accounting for frame time here)
      InstrLang5.frameNStart = frameN;  // exact frame index
      
      InstrLang5.setAutoDraw(true);
    }

    
    // *InstrLang6* updates
    if (t >= 0.0 && InstrLang6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrLang6.tStart = t;  // (not accounting for frame time here)
      InstrLang6.frameNStart = frameN;  // exact frame index
      
      InstrLang6.setAutoDraw(true);
    }

    
    // *InstrLang7* updates
    if (t >= 0.0 && InstrLang7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrLang7.tStart = t;  // (not accounting for frame time here)
      InstrLang7.frameNStart = frameN;  // exact frame index
      
      InstrLang7.setAutoDraw(true);
    }

    
    // *fluentLang* updates
    if (t >= 0.0 && fluentLang.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fluentLang.tStart = t;  // (not accounting for frame time here)
      fluentLang.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fluentLang.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fluentLang.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fluentLang.clearEvents(); });
    }

    if (fluentLang.status === PsychoJS.Status.STARTED) {
      let theseKeys = fluentLang.getKeys({keyList: ['1', '2', '3', '4', '5', '6', 'space'], waitRelease: false});
      _fluentLang_allKeys = _fluentLang_allKeys.concat(theseKeys);
      if (_fluentLang_allKeys.length > 0) {
        fluentLang.keys = _fluentLang_allKeys[_fluentLang_allKeys.length - 1].name;  // just the last key pressed
        fluentLang.rt = _fluentLang_allKeys[_fluentLang_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *spaceTextLang* updates
    if (t >= 0.0 && spaceTextLang.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      spaceTextLang.tStart = t;  // (not accounting for frame time here)
      spaceTextLang.frameNStart = frameN;  // exact frame index
      
      spaceTextLang.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LanguagesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LanguagesRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Languages'-------
    LanguagesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fluentLang.keys', fluentLang.keys);
    if (typeof fluentLang.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fluentLang.rt', fluentLang.rt);
        routineTimer.reset();
        }
    
    fluentLang.stop();
    // the Routine "Languages" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _spaceKey_allKeys;
var gotValidClick;
var ProficiencyEngComponents;
function ProficiencyEngRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ProficiencyEng'-------
    t = 0;
    ProficiencyEngClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    engSpeak.reset()
    engRead.reset()
    engWrite.reset()
    spaceKey.keys = undefined;
    spaceKey.rt = undefined;
    _spaceKey_allKeys = [];
    // setup some python lists for storing info about the mouseProf
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    ProficiencyEngComponents = [];
    ProficiencyEngComponents.push(textProficiencyEng);
    ProficiencyEngComponents.push(MouseInstruction);
    ProficiencyEngComponents.push(engSpeak);
    ProficiencyEngComponents.push(engRead);
    ProficiencyEngComponents.push(engWrite);
    ProficiencyEngComponents.push(eSpeakLabel);
    ProficiencyEngComponents.push(eReadLabel);
    ProficiencyEngComponents.push(eWriteLabel);
    ProficiencyEngComponents.push(spaceText);
    ProficiencyEngComponents.push(spaceKey);
    ProficiencyEngComponents.push(mouseProf);
    
    ProficiencyEngComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function ProficiencyEngRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ProficiencyEng'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ProficiencyEngClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textProficiencyEng* updates
    if (t >= 0.0 && textProficiencyEng.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textProficiencyEng.tStart = t;  // (not accounting for frame time here)
      textProficiencyEng.frameNStart = frameN;  // exact frame index
      
      textProficiencyEng.setAutoDraw(true);
    }

    
    // *MouseInstruction* updates
    if (t >= 0.0 && MouseInstruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MouseInstruction.tStart = t;  // (not accounting for frame time here)
      MouseInstruction.frameNStart = frameN;  // exact frame index
      
      MouseInstruction.setAutoDraw(true);
    }

    
    // *engSpeak* updates
    if (t >= 0.0 && engSpeak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engSpeak.tStart = t;  // (not accounting for frame time here)
      engSpeak.frameNStart = frameN;  // exact frame index
      
      engSpeak.setAutoDraw(true);
    }

    
    // *engRead* updates
    if (t >= 0.0 && engRead.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engRead.tStart = t;  // (not accounting for frame time here)
      engRead.frameNStart = frameN;  // exact frame index
      
      engRead.setAutoDraw(true);
    }

    
    // *engWrite* updates
    if (t >= 0.0 && engWrite.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engWrite.tStart = t;  // (not accounting for frame time here)
      engWrite.frameNStart = frameN;  // exact frame index
      
      engWrite.setAutoDraw(true);
    }

    
    // *eSpeakLabel* updates
    if (t >= 0.0 && eSpeakLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eSpeakLabel.tStart = t;  // (not accounting for frame time here)
      eSpeakLabel.frameNStart = frameN;  // exact frame index
      
      eSpeakLabel.setAutoDraw(true);
    }

    
    // *eReadLabel* updates
    if (t >= 0.0 && eReadLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eReadLabel.tStart = t;  // (not accounting for frame time here)
      eReadLabel.frameNStart = frameN;  // exact frame index
      
      eReadLabel.setAutoDraw(true);
    }

    
    // *eWriteLabel* updates
    if (t >= 0.0 && eWriteLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eWriteLabel.tStart = t;  // (not accounting for frame time here)
      eWriteLabel.frameNStart = frameN;  // exact frame index
      
      eWriteLabel.setAutoDraw(true);
    }

    
    // *spaceText* updates
    if (t >= 0.0 && spaceText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      spaceText.tStart = t;  // (not accounting for frame time here)
      spaceText.frameNStart = frameN;  // exact frame index
      
      spaceText.setAutoDraw(true);
    }

    
    // *spaceKey* updates
    if (t >= 0.0 && spaceKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      spaceKey.tStart = t;  // (not accounting for frame time here)
      spaceKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { spaceKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { spaceKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { spaceKey.clearEvents(); });
    }

    if (spaceKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = spaceKey.getKeys({keyList: ['space'], waitRelease: false});
      _spaceKey_allKeys = _spaceKey_allKeys.concat(theseKeys);
      if (_spaceKey_allKeys.length > 0) {
        spaceKey.keys = _spaceKey_allKeys[_spaceKey_allKeys.length - 1].name;  // just the last key pressed
        spaceKey.rt = _spaceKey_allKeys[_spaceKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ProficiencyEngComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ProficiencyEngRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ProficiencyEng'-------
    ProficiencyEngComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('engSpeak.response', engSpeak.getRating());
    psychoJS.experiment.addData('engRead.response', engRead.getRating());
    psychoJS.experiment.addData('engWrite.response', engWrite.getRating());
    // store data for thisExp (ExperimentHandler)
    // the Routine "ProficiencyEng" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyActivitiesEng_allKeys;
var ActivitiesEngComponents;
function ActivitiesEngRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ActivitiesEng'-------
    t = 0;
    ActivitiesEngClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    engSpeakFreq.reset()
    engListenFreq.reset()
    engReadFreq.reset()
    engWriteFreq.reset()
    keyActivitiesEng.keys = undefined;
    keyActivitiesEng.rt = undefined;
    _keyActivitiesEng_allKeys = [];
    // setup some python lists for storing info about the mouseActEng
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    ActivitiesEngComponents = [];
    ActivitiesEngComponents.push(textActivitiesEng);
    ActivitiesEngComponents.push(text_6);
    ActivitiesEngComponents.push(engSpeakFreq);
    ActivitiesEngComponents.push(engListenFreq);
    ActivitiesEngComponents.push(engReadFreq);
    ActivitiesEngComponents.push(engWriteFreq);
    ActivitiesEngComponents.push(engSpeakLabel);
    ActivitiesEngComponents.push(engListenLabel);
    ActivitiesEngComponents.push(engReadLabel);
    ActivitiesEngComponents.push(engWriteLabel);
    ActivitiesEngComponents.push(textSpaceActivitiesEng);
    ActivitiesEngComponents.push(keyActivitiesEng);
    ActivitiesEngComponents.push(mouseActEng);
    
    ActivitiesEngComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function ActivitiesEngRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ActivitiesEng'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ActivitiesEngClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textActivitiesEng* updates
    if (t >= 0.0 && textActivitiesEng.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textActivitiesEng.tStart = t;  // (not accounting for frame time here)
      textActivitiesEng.frameNStart = frameN;  // exact frame index
      
      textActivitiesEng.setAutoDraw(true);
    }

    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    
    // *engSpeakFreq* updates
    if (t >= 0.0 && engSpeakFreq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engSpeakFreq.tStart = t;  // (not accounting for frame time here)
      engSpeakFreq.frameNStart = frameN;  // exact frame index
      
      engSpeakFreq.setAutoDraw(true);
    }

    
    // *engListenFreq* updates
    if (t >= 0.0 && engListenFreq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engListenFreq.tStart = t;  // (not accounting for frame time here)
      engListenFreq.frameNStart = frameN;  // exact frame index
      
      engListenFreq.setAutoDraw(true);
    }

    
    // *engReadFreq* updates
    if (t >= 0.0 && engReadFreq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engReadFreq.tStart = t;  // (not accounting for frame time here)
      engReadFreq.frameNStart = frameN;  // exact frame index
      
      engReadFreq.setAutoDraw(true);
    }

    
    // *engWriteFreq* updates
    if (t >= 0.0 && engWriteFreq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engWriteFreq.tStart = t;  // (not accounting for frame time here)
      engWriteFreq.frameNStart = frameN;  // exact frame index
      
      engWriteFreq.setAutoDraw(true);
    }

    
    // *engSpeakLabel* updates
    if (t >= 0.0 && engSpeakLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engSpeakLabel.tStart = t;  // (not accounting for frame time here)
      engSpeakLabel.frameNStart = frameN;  // exact frame index
      
      engSpeakLabel.setAutoDraw(true);
    }

    
    // *engListenLabel* updates
    if (t >= 0.0 && engListenLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engListenLabel.tStart = t;  // (not accounting for frame time here)
      engListenLabel.frameNStart = frameN;  // exact frame index
      
      engListenLabel.setAutoDraw(true);
    }

    
    // *engReadLabel* updates
    if (t >= 0.0 && engReadLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engReadLabel.tStart = t;  // (not accounting for frame time here)
      engReadLabel.frameNStart = frameN;  // exact frame index
      
      engReadLabel.setAutoDraw(true);
    }

    
    // *engWriteLabel* updates
    if (t >= 0.0 && engWriteLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      engWriteLabel.tStart = t;  // (not accounting for frame time here)
      engWriteLabel.frameNStart = frameN;  // exact frame index
      
      engWriteLabel.setAutoDraw(true);
    }

    
    // *textSpaceActivitiesEng* updates
    if (t >= 0.0 && textSpaceActivitiesEng.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpaceActivitiesEng.tStart = t;  // (not accounting for frame time here)
      textSpaceActivitiesEng.frameNStart = frameN;  // exact frame index
      
      textSpaceActivitiesEng.setAutoDraw(true);
    }

    
    // *keyActivitiesEng* updates
    if (t >= 0.0 && keyActivitiesEng.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyActivitiesEng.tStart = t;  // (not accounting for frame time here)
      keyActivitiesEng.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyActivitiesEng.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyActivitiesEng.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyActivitiesEng.clearEvents(); });
    }

    if (keyActivitiesEng.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyActivitiesEng.getKeys({keyList: ['space'], waitRelease: false});
      _keyActivitiesEng_allKeys = _keyActivitiesEng_allKeys.concat(theseKeys);
      if (_keyActivitiesEng_allKeys.length > 0) {
        keyActivitiesEng.keys = _keyActivitiesEng_allKeys[_keyActivitiesEng_allKeys.length - 1].name;  // just the last key pressed
        keyActivitiesEng.rt = _keyActivitiesEng_allKeys[_keyActivitiesEng_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ActivitiesEngComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ActivitiesEngRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ActivitiesEng'-------
    ActivitiesEngComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('engSpeakFreq.response', engSpeakFreq.getRating());
    psychoJS.experiment.addData('engListenFreq.response', engListenFreq.getRating());
    psychoJS.experiment.addData('engReadFreq.response', engReadFreq.getRating());
    psychoJS.experiment.addData('engWriteFreq.response', engWriteFreq.getRating());
    // store data for thisExp (ExperimentHandler)
    // the Routine "ActivitiesEng" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_reading_allKeys;
var ReadingEngComponents;
function ReadingEngRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ReadingEng'-------
    t = 0;
    ReadingEngClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    slider_engReadHrs.reset()
    key_reading.keys = undefined;
    key_reading.rt = undefined;
    _key_reading_allKeys = [];
    // keep track of which components have finished
    ReadingEngComponents = [];
    ReadingEngComponents.push(hoursReading);
    ReadingEngComponents.push(text_8);
    ReadingEngComponents.push(slider_engReadHrs);
    ReadingEngComponents.push(space);
    ReadingEngComponents.push(key_reading);
    
    ReadingEngComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function ReadingEngRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ReadingEng'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ReadingEngClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *hoursReading* updates
    if (t >= 0.0 && hoursReading.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hoursReading.tStart = t;  // (not accounting for frame time here)
      hoursReading.frameNStart = frameN;  // exact frame index
      
      hoursReading.setAutoDraw(true);
    }

    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    
    // *slider_engReadHrs* updates
    if (t >= 0.0 && slider_engReadHrs.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_engReadHrs.tStart = t;  // (not accounting for frame time here)
      slider_engReadHrs.frameNStart = frameN;  // exact frame index
      
      slider_engReadHrs.setAutoDraw(true);
    }

    
    // *space* updates
    if (t >= 0.0 && space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space.tStart = t;  // (not accounting for frame time here)
      space.frameNStart = frameN;  // exact frame index
      
      space.setAutoDraw(true);
    }

    
    // *key_reading* updates
    if (t >= 0.0 && key_reading.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_reading.tStart = t;  // (not accounting for frame time here)
      key_reading.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_reading.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_reading.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_reading.clearEvents(); });
    }

    if (key_reading.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_reading.getKeys({keyList: ['space'], waitRelease: false});
      _key_reading_allKeys = _key_reading_allKeys.concat(theseKeys);
      if (_key_reading_allKeys.length > 0) {
        key_reading.keys = _key_reading_allKeys[_key_reading_allKeys.length - 1].name;  // just the last key pressed
        key_reading.rt = _key_reading_allKeys[_key_reading_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ReadingEngComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ReadingEngRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ReadingEng'-------
    ReadingEngComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_engReadHrs.response', slider_engReadHrs.getRating());
    // the Routine "ReadingEng" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keySpaceAr_allKeys;
var ProficiencyArComponents;
function ProficiencyArRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ProficiencyAr'-------
    t = 0;
    ProficiencyArClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    ArSpeak.reset()
    ArRead.reset()
    ArWrite.reset()
    keySpaceAr.keys = undefined;
    keySpaceAr.rt = undefined;
    _keySpaceAr_allKeys = [];
    // keep track of which components have finished
    ProficiencyArComponents = [];
    ProficiencyArComponents.push(textProficiencyArb);
    ProficiencyArComponents.push(text_7);
    ProficiencyArComponents.push(ArSpeak);
    ProficiencyArComponents.push(ArRead);
    ProficiencyArComponents.push(ArWrite);
    ProficiencyArComponents.push(arSpeakLabel);
    ProficiencyArComponents.push(arReadLabel);
    ProficiencyArComponents.push(arWriteLabel);
    ProficiencyArComponents.push(textSpaceAr);
    ProficiencyArComponents.push(keySpaceAr);
    
    ProficiencyArComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function ProficiencyArRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ProficiencyAr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ProficiencyArClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textProficiencyArb* updates
    if (t >= 0.0 && textProficiencyArb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textProficiencyArb.tStart = t;  // (not accounting for frame time here)
      textProficiencyArb.frameNStart = frameN;  // exact frame index
      
      textProficiencyArb.setAutoDraw(true);
    }

    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *ArSpeak* updates
    if (t >= 0.0 && ArSpeak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ArSpeak.tStart = t;  // (not accounting for frame time here)
      ArSpeak.frameNStart = frameN;  // exact frame index
      
      ArSpeak.setAutoDraw(true);
    }

    
    // *ArRead* updates
    if (t >= 0.0 && ArRead.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ArRead.tStart = t;  // (not accounting for frame time here)
      ArRead.frameNStart = frameN;  // exact frame index
      
      ArRead.setAutoDraw(true);
    }

    
    // *ArWrite* updates
    if (t >= 0.0 && ArWrite.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ArWrite.tStart = t;  // (not accounting for frame time here)
      ArWrite.frameNStart = frameN;  // exact frame index
      
      ArWrite.setAutoDraw(true);
    }

    
    // *arSpeakLabel* updates
    if (t >= 0.0 && arSpeakLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arSpeakLabel.tStart = t;  // (not accounting for frame time here)
      arSpeakLabel.frameNStart = frameN;  // exact frame index
      
      arSpeakLabel.setAutoDraw(true);
    }

    
    // *arReadLabel* updates
    if (t >= 0.0 && arReadLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arReadLabel.tStart = t;  // (not accounting for frame time here)
      arReadLabel.frameNStart = frameN;  // exact frame index
      
      arReadLabel.setAutoDraw(true);
    }

    
    // *arWriteLabel* updates
    if (t >= 0.0 && arWriteLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arWriteLabel.tStart = t;  // (not accounting for frame time here)
      arWriteLabel.frameNStart = frameN;  // exact frame index
      
      arWriteLabel.setAutoDraw(true);
    }

    
    // *textSpaceAr* updates
    if (t >= 0.0 && textSpaceAr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpaceAr.tStart = t;  // (not accounting for frame time here)
      textSpaceAr.frameNStart = frameN;  // exact frame index
      
      textSpaceAr.setAutoDraw(true);
    }

    
    // *keySpaceAr* updates
    if (t >= 0.0 && keySpaceAr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keySpaceAr.tStart = t;  // (not accounting for frame time here)
      keySpaceAr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keySpaceAr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keySpaceAr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keySpaceAr.clearEvents(); });
    }

    if (keySpaceAr.status === PsychoJS.Status.STARTED) {
      let theseKeys = keySpaceAr.getKeys({keyList: ['space'], waitRelease: false});
      _keySpaceAr_allKeys = _keySpaceAr_allKeys.concat(theseKeys);
      if (_keySpaceAr_allKeys.length > 0) {
        keySpaceAr.keys = _keySpaceAr_allKeys[_keySpaceAr_allKeys.length - 1].name;  // just the last key pressed
        keySpaceAr.rt = _keySpaceAr_allKeys[_keySpaceAr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ProficiencyArComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ProficiencyArRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ProficiencyAr'-------
    ProficiencyArComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ArSpeak.response', ArSpeak.getRating());
    psychoJS.experiment.addData('ArRead.response', ArRead.getRating());
    psychoJS.experiment.addData('ArWrite.response', ArWrite.getRating());
    // the Routine "ProficiencyAr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keySpaceActivitiesAr_allKeys;
var ActivitiesArComponents;
function ActivitiesArRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ActivitiesAr'-------
    t = 0;
    ActivitiesArClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    arSpeakFreq.reset()
    arListenFreq.reset()
    arReadFreq.reset()
    arWriteFreq.reset()
    keySpaceActivitiesAr.keys = undefined;
    keySpaceActivitiesAr.rt = undefined;
    _keySpaceActivitiesAr_allKeys = [];
    // keep track of which components have finished
    ActivitiesArComponents = [];
    ActivitiesArComponents.push(textActivitiesAr);
    ActivitiesArComponents.push(text_9);
    ActivitiesArComponents.push(arSpeakFreq);
    ActivitiesArComponents.push(arListenFreq);
    ActivitiesArComponents.push(arReadFreq);
    ActivitiesArComponents.push(arWriteFreq);
    ActivitiesArComponents.push(aSpeakLabel);
    ActivitiesArComponents.push(aListenLabel);
    ActivitiesArComponents.push(aReadLabel);
    ActivitiesArComponents.push(aWriteLabel);
    ActivitiesArComponents.push(textSpaceActivitiesAr);
    ActivitiesArComponents.push(keySpaceActivitiesAr);
    
    ActivitiesArComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function ActivitiesArRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ActivitiesAr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ActivitiesArClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textActivitiesAr* updates
    if (t >= 0.0 && textActivitiesAr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textActivitiesAr.tStart = t;  // (not accounting for frame time here)
      textActivitiesAr.frameNStart = frameN;  // exact frame index
      
      textActivitiesAr.setAutoDraw(true);
    }

    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    
    // *arSpeakFreq* updates
    if (t >= 0.0 && arSpeakFreq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arSpeakFreq.tStart = t;  // (not accounting for frame time here)
      arSpeakFreq.frameNStart = frameN;  // exact frame index
      
      arSpeakFreq.setAutoDraw(true);
    }

    
    // *arListenFreq* updates
    if (t >= 0.0 && arListenFreq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arListenFreq.tStart = t;  // (not accounting for frame time here)
      arListenFreq.frameNStart = frameN;  // exact frame index
      
      arListenFreq.setAutoDraw(true);
    }

    
    // *arReadFreq* updates
    if (t >= 0.0 && arReadFreq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arReadFreq.tStart = t;  // (not accounting for frame time here)
      arReadFreq.frameNStart = frameN;  // exact frame index
      
      arReadFreq.setAutoDraw(true);
    }

    
    // *arWriteFreq* updates
    if (t >= 0.0 && arWriteFreq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arWriteFreq.tStart = t;  // (not accounting for frame time here)
      arWriteFreq.frameNStart = frameN;  // exact frame index
      
      arWriteFreq.setAutoDraw(true);
    }

    
    // *aSpeakLabel* updates
    if (t >= 0.0 && aSpeakLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      aSpeakLabel.tStart = t;  // (not accounting for frame time here)
      aSpeakLabel.frameNStart = frameN;  // exact frame index
      
      aSpeakLabel.setAutoDraw(true);
    }

    
    // *aListenLabel* updates
    if (t >= 0.0 && aListenLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      aListenLabel.tStart = t;  // (not accounting for frame time here)
      aListenLabel.frameNStart = frameN;  // exact frame index
      
      aListenLabel.setAutoDraw(true);
    }

    
    // *aReadLabel* updates
    if (t >= 0.0 && aReadLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      aReadLabel.tStart = t;  // (not accounting for frame time here)
      aReadLabel.frameNStart = frameN;  // exact frame index
      
      aReadLabel.setAutoDraw(true);
    }

    
    // *aWriteLabel* updates
    if (t >= 0.0 && aWriteLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      aWriteLabel.tStart = t;  // (not accounting for frame time here)
      aWriteLabel.frameNStart = frameN;  // exact frame index
      
      aWriteLabel.setAutoDraw(true);
    }

    
    // *textSpaceActivitiesAr* updates
    if (t >= 0.0 && textSpaceActivitiesAr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpaceActivitiesAr.tStart = t;  // (not accounting for frame time here)
      textSpaceActivitiesAr.frameNStart = frameN;  // exact frame index
      
      textSpaceActivitiesAr.setAutoDraw(true);
    }

    
    // *keySpaceActivitiesAr* updates
    if (t >= 0.0 && keySpaceActivitiesAr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keySpaceActivitiesAr.tStart = t;  // (not accounting for frame time here)
      keySpaceActivitiesAr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keySpaceActivitiesAr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keySpaceActivitiesAr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keySpaceActivitiesAr.clearEvents(); });
    }

    if (keySpaceActivitiesAr.status === PsychoJS.Status.STARTED) {
      let theseKeys = keySpaceActivitiesAr.getKeys({keyList: ['space'], waitRelease: false});
      _keySpaceActivitiesAr_allKeys = _keySpaceActivitiesAr_allKeys.concat(theseKeys);
      if (_keySpaceActivitiesAr_allKeys.length > 0) {
        keySpaceActivitiesAr.keys = _keySpaceActivitiesAr_allKeys[_keySpaceActivitiesAr_allKeys.length - 1].name;  // just the last key pressed
        keySpaceActivitiesAr.rt = _keySpaceActivitiesAr_allKeys[_keySpaceActivitiesAr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ActivitiesArComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ActivitiesArRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ActivitiesAr'-------
    ActivitiesArComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('arSpeakFreq.response', arSpeakFreq.getRating());
    psychoJS.experiment.addData('arListenFreq.response', arListenFreq.getRating());
    psychoJS.experiment.addData('arReadFreq.response', arReadFreq.getRating());
    psychoJS.experiment.addData('arWriteFreq.response', arWriteFreq.getRating());
    // the Routine "ActivitiesAr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_space_allKeys;
var ReadingArComponents;
function ReadingArRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ReadingAr'-------
    t = 0;
    ReadingArClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_space.keys = undefined;
    key_space.rt = undefined;
    _key_space_allKeys = [];
    arReadHrs.reset()
    // keep track of which components have finished
    ReadingArComponents = [];
    ReadingArComponents.push(readingAr);
    ReadingArComponents.push(text_10);
    ReadingArComponents.push(spaceContinue_3);
    ReadingArComponents.push(key_space);
    ReadingArComponents.push(arReadHrs);
    
    ReadingArComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function ReadingArRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ReadingAr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ReadingArClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *readingAr* updates
    if (t >= 0.0 && readingAr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      readingAr.tStart = t;  // (not accounting for frame time here)
      readingAr.frameNStart = frameN;  // exact frame index
      
      readingAr.setAutoDraw(true);
    }

    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }

    
    // *spaceContinue_3* updates
    if (t >= 0.0 && spaceContinue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      spaceContinue_3.tStart = t;  // (not accounting for frame time here)
      spaceContinue_3.frameNStart = frameN;  // exact frame index
      
      spaceContinue_3.setAutoDraw(true);
    }

    
    // *key_space* updates
    if (t >= 0.0 && key_space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_space.tStart = t;  // (not accounting for frame time here)
      key_space.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_space.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_space.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_space.clearEvents(); });
    }

    if (key_space.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_space.getKeys({keyList: ['space'], waitRelease: false});
      _key_space_allKeys = _key_space_allKeys.concat(theseKeys);
      if (_key_space_allKeys.length > 0) {
        key_space.keys = _key_space_allKeys[_key_space_allKeys.length - 1].name;  // just the last key pressed
        key_space.rt = _key_space_allKeys[_key_space_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *arReadHrs* updates
    if (t >= 0.0 && arReadHrs.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arReadHrs.tStart = t;  // (not accounting for frame time here)
      arReadHrs.frameNStart = frameN;  // exact frame index
      
      arReadHrs.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ReadingArComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ReadingArRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ReadingAr'-------
    ReadingArComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('arReadHrs.response', arReadHrs.getRating());
    // the Routine "ReadingAr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _arbCountryTime_allKeys;
var _key_space_3_allKeys;
var TimeArComponents;
function TimeArRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'TimeAr'-------
    t = 0;
    TimeArClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    arbCountryTime.keys = undefined;
    arbCountryTime.rt = undefined;
    _arbCountryTime_allKeys = [];
    key_space_3.keys = undefined;
    key_space_3.rt = undefined;
    _key_space_3_allKeys = [];
    // keep track of which components have finished
    TimeArComponents = [];
    TimeArComponents.push(textLongCountAr);
    TimeArComponents.push(spaceContinue_2);
    TimeArComponents.push(Option1);
    TimeArComponents.push(Option2);
    TimeArComponents.push(Option3);
    TimeArComponents.push(Option4);
    TimeArComponents.push(Option5);
    TimeArComponents.push(arbCountryTime);
    TimeArComponents.push(key_space_3);
    
    TimeArComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function TimeArRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'TimeAr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = TimeArClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textLongCountAr* updates
    if (t >= 0.0 && textLongCountAr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textLongCountAr.tStart = t;  // (not accounting for frame time here)
      textLongCountAr.frameNStart = frameN;  // exact frame index
      
      textLongCountAr.setAutoDraw(true);
    }

    
    // *spaceContinue_2* updates
    if (t >= 0.0 && spaceContinue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      spaceContinue_2.tStart = t;  // (not accounting for frame time here)
      spaceContinue_2.frameNStart = frameN;  // exact frame index
      
      spaceContinue_2.setAutoDraw(true);
    }

    
    // *Option1* updates
    if (t >= 0.0 && Option1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Option1.tStart = t;  // (not accounting for frame time here)
      Option1.frameNStart = frameN;  // exact frame index
      
      Option1.setAutoDraw(true);
    }

    
    // *Option2* updates
    if (t >= 0.0 && Option2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Option2.tStart = t;  // (not accounting for frame time here)
      Option2.frameNStart = frameN;  // exact frame index
      
      Option2.setAutoDraw(true);
    }

    
    // *Option3* updates
    if (t >= 0.0 && Option3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Option3.tStart = t;  // (not accounting for frame time here)
      Option3.frameNStart = frameN;  // exact frame index
      
      Option3.setAutoDraw(true);
    }

    
    // *Option4* updates
    if (t >= 0.0 && Option4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Option4.tStart = t;  // (not accounting for frame time here)
      Option4.frameNStart = frameN;  // exact frame index
      
      Option4.setAutoDraw(true);
    }

    
    // *Option5* updates
    if (t >= 0.0 && Option5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Option5.tStart = t;  // (not accounting for frame time here)
      Option5.frameNStart = frameN;  // exact frame index
      
      Option5.setAutoDraw(true);
    }

    
    // *arbCountryTime* updates
    if (t >= 0.0 && arbCountryTime.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arbCountryTime.tStart = t;  // (not accounting for frame time here)
      arbCountryTime.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { arbCountryTime.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { arbCountryTime.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { arbCountryTime.clearEvents(); });
    }

    if (arbCountryTime.status === PsychoJS.Status.STARTED) {
      let theseKeys = arbCountryTime.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _arbCountryTime_allKeys = _arbCountryTime_allKeys.concat(theseKeys);
      if (_arbCountryTime_allKeys.length > 0) {
        arbCountryTime.keys = _arbCountryTime_allKeys[_arbCountryTime_allKeys.length - 1].name;  // just the last key pressed
        arbCountryTime.rt = _arbCountryTime_allKeys[_arbCountryTime_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *key_space_3* updates
    if (t >= 0.0 && key_space_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_space_3.tStart = t;  // (not accounting for frame time here)
      key_space_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_space_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_space_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_space_3.clearEvents(); });
    }

    if (key_space_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_space_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_space_3_allKeys = _key_space_3_allKeys.concat(theseKeys);
      if (_key_space_3_allKeys.length > 0) {
        key_space_3.keys = _key_space_3_allKeys[_key_space_3_allKeys.length - 1].name;  // just the last key pressed
        key_space_3.rt = _key_space_3_allKeys[_key_space_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TimeArComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TimeArRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'TimeAr'-------
    TimeArComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('arbCountryTime.keys', arbCountryTime.keys);
    if (typeof arbCountryTime.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('arbCountryTime.rt', arbCountryTime.rt);
        routineTimer.reset();
        }
    
    arbCountryTime.stop();
    // the Routine "TimeAr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keySpaceHand_allKeys;
var HandednessComponents;
function HandednessRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Handedness'-------
    t = 0;
    HandednessClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    writeHand.reset()
    throwHand.reset()
    toothHand.reset()
    spoonHand.reset()
    keySpaceHand.keys = undefined;
    keySpaceHand.rt = undefined;
    _keySpaceHand_allKeys = [];
    // keep track of which components have finished
    HandednessComponents = [];
    HandednessComponents.push(textHandedness);
    HandednessComponents.push(writeHand);
    HandednessComponents.push(throwHand);
    HandednessComponents.push(toothHand);
    HandednessComponents.push(spoonHand);
    HandednessComponents.push(writeHandLabel);
    HandednessComponents.push(throwHandLabel);
    HandednessComponents.push(toothHandLabel);
    HandednessComponents.push(spoonHandLabel);
    HandednessComponents.push(textSpaceHand);
    HandednessComponents.push(keySpaceHand);
    
    HandednessComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function HandednessRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Handedness'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = HandednessClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textHandedness* updates
    if (t >= 0.0 && textHandedness.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textHandedness.tStart = t;  // (not accounting for frame time here)
      textHandedness.frameNStart = frameN;  // exact frame index
      
      textHandedness.setAutoDraw(true);
    }

    
    // *writeHand* updates
    if (t >= 0.0 && writeHand.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      writeHand.tStart = t;  // (not accounting for frame time here)
      writeHand.frameNStart = frameN;  // exact frame index
      
      writeHand.setAutoDraw(true);
    }

    
    // *throwHand* updates
    if (t >= 0.0 && throwHand.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      throwHand.tStart = t;  // (not accounting for frame time here)
      throwHand.frameNStart = frameN;  // exact frame index
      
      throwHand.setAutoDraw(true);
    }

    
    // *toothHand* updates
    if (t >= 0.0 && toothHand.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      toothHand.tStart = t;  // (not accounting for frame time here)
      toothHand.frameNStart = frameN;  // exact frame index
      
      toothHand.setAutoDraw(true);
    }

    
    // *spoonHand* updates
    if (t >= 0.0 && spoonHand.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      spoonHand.tStart = t;  // (not accounting for frame time here)
      spoonHand.frameNStart = frameN;  // exact frame index
      
      spoonHand.setAutoDraw(true);
    }

    
    // *writeHandLabel* updates
    if (t >= 0.0 && writeHandLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      writeHandLabel.tStart = t;  // (not accounting for frame time here)
      writeHandLabel.frameNStart = frameN;  // exact frame index
      
      writeHandLabel.setAutoDraw(true);
    }

    
    // *throwHandLabel* updates
    if (t >= 0.0 && throwHandLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      throwHandLabel.tStart = t;  // (not accounting for frame time here)
      throwHandLabel.frameNStart = frameN;  // exact frame index
      
      throwHandLabel.setAutoDraw(true);
    }

    
    // *toothHandLabel* updates
    if (t >= 0.0 && toothHandLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      toothHandLabel.tStart = t;  // (not accounting for frame time here)
      toothHandLabel.frameNStart = frameN;  // exact frame index
      
      toothHandLabel.setAutoDraw(true);
    }

    
    // *spoonHandLabel* updates
    if (t >= 0.0 && spoonHandLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      spoonHandLabel.tStart = t;  // (not accounting for frame time here)
      spoonHandLabel.frameNStart = frameN;  // exact frame index
      
      spoonHandLabel.setAutoDraw(true);
    }

    
    // *textSpaceHand* updates
    if (t >= 0.0 && textSpaceHand.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpaceHand.tStart = t;  // (not accounting for frame time here)
      textSpaceHand.frameNStart = frameN;  // exact frame index
      
      textSpaceHand.setAutoDraw(true);
    }

    
    // *keySpaceHand* updates
    if (t >= 0.0 && keySpaceHand.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keySpaceHand.tStart = t;  // (not accounting for frame time here)
      keySpaceHand.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keySpaceHand.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keySpaceHand.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keySpaceHand.clearEvents(); });
    }

    if (keySpaceHand.status === PsychoJS.Status.STARTED) {
      let theseKeys = keySpaceHand.getKeys({keyList: ['space'], waitRelease: false});
      _keySpaceHand_allKeys = _keySpaceHand_allKeys.concat(theseKeys);
      if (_keySpaceHand_allKeys.length > 0) {
        keySpaceHand.keys = _keySpaceHand_allKeys[_keySpaceHand_allKeys.length - 1].name;  // just the last key pressed
        keySpaceHand.rt = _keySpaceHand_allKeys[_keySpaceHand_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    HandednessComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function HandednessRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Handedness'-------
    HandednessComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('writeHand.response', writeHand.getRating());
    psychoJS.experiment.addData('throwHand.response', throwHand.getRating());
    psychoJS.experiment.addData('toothHand.response', toothHand.getRating());
    psychoJS.experiment.addData('spoonHand.response', spoonHand.getRating());
    // the Routine "Handedness" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _finishQKey_allKeys;
var Q_FinishComponents;
function Q_FinishRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Q_Finish'-------
    t = 0;
    Q_FinishClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    finishQKey.keys = undefined;
    finishQKey.rt = undefined;
    _finishQKey_allKeys = [];
    // keep track of which components have finished
    Q_FinishComponents = [];
    Q_FinishComponents.push(QDone);
    Q_FinishComponents.push(text_11);
    Q_FinishComponents.push(finishQKey);
    
    Q_FinishComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function Q_FinishRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Q_Finish'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Q_FinishClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *QDone* updates
    if (t >= 0.0 && QDone.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      QDone.tStart = t;  // (not accounting for frame time here)
      QDone.frameNStart = frameN;  // exact frame index
      
      QDone.setAutoDraw(true);
    }

    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }

    
    // *finishQKey* updates
    if (t >= 0.0 && finishQKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      finishQKey.tStart = t;  // (not accounting for frame time here)
      finishQKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { finishQKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { finishQKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { finishQKey.clearEvents(); });
    }

    if (finishQKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = finishQKey.getKeys({keyList: ['space'], waitRelease: false});
      _finishQKey_allKeys = _finishQKey_allKeys.concat(theseKeys);
      if (_finishQKey_allKeys.length > 0) {
        finishQKey.keys = _finishQKey_allKeys[_finishQKey_allKeys.length - 1].name;  // just the last key pressed
        finishQKey.rt = _finishQKey_allKeys[_finishQKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Q_FinishComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Q_FinishRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Q_Finish'-------
    Q_FinishComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Q_Finish" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _SpacePracticInst_allKeys;
var PracticeInstrComponents;
function PracticeInstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'PracticeInstr'-------
    t = 0;
    PracticeInstrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    SpacePracticInst.keys = undefined;
    SpacePracticInst.rt = undefined;
    _SpacePracticInst_allKeys = [];
    // setup some python lists for storing info about the mouse
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    PracticeInstrComponents = [];
    PracticeInstrComponents.push(practiceInstr);
    PracticeInstrComponents.push(textSpacePractInstr);
    PracticeInstrComponents.push(practiceInst2);
    PracticeInstrComponents.push(practiceInstr3);
    PracticeInstrComponents.push(practiceInstr4);
    PracticeInstrComponents.push(practiceInstr5);
    PracticeInstrComponents.push(SpacePracticInst);
    PracticeInstrComponents.push(mouse);
    
    PracticeInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function PracticeInstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'PracticeInstr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PracticeInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practiceInstr* updates
    if (t >= 0.0 && practiceInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceInstr.tStart = t;  // (not accounting for frame time here)
      practiceInstr.frameNStart = frameN;  // exact frame index
      
      practiceInstr.setAutoDraw(true);
    }

    
    // *textSpacePractInstr* updates
    if (t >= 0.0 && textSpacePractInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpacePractInstr.tStart = t;  // (not accounting for frame time here)
      textSpacePractInstr.frameNStart = frameN;  // exact frame index
      
      textSpacePractInstr.setAutoDraw(true);
    }

    
    // *practiceInst2* updates
    if (t >= 0.0 && practiceInst2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceInst2.tStart = t;  // (not accounting for frame time here)
      practiceInst2.frameNStart = frameN;  // exact frame index
      
      practiceInst2.setAutoDraw(true);
    }

    
    // *practiceInstr3* updates
    if (t >= 0.0 && practiceInstr3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceInstr3.tStart = t;  // (not accounting for frame time here)
      practiceInstr3.frameNStart = frameN;  // exact frame index
      
      practiceInstr3.setAutoDraw(true);
    }

    
    // *practiceInstr4* updates
    if (t >= 0.0 && practiceInstr4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceInstr4.tStart = t;  // (not accounting for frame time here)
      practiceInstr4.frameNStart = frameN;  // exact frame index
      
      practiceInstr4.setAutoDraw(true);
    }

    
    // *practiceInstr5* updates
    if (t >= 0.0 && practiceInstr5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceInstr5.tStart = t;  // (not accounting for frame time here)
      practiceInstr5.frameNStart = frameN;  // exact frame index
      
      practiceInstr5.setAutoDraw(true);
    }

    
    // *SpacePracticInst* updates
    if (t >= 0.0 && SpacePracticInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SpacePracticInst.tStart = t;  // (not accounting for frame time here)
      SpacePracticInst.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SpacePracticInst.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SpacePracticInst.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SpacePracticInst.clearEvents(); });
    }

    if (SpacePracticInst.status === PsychoJS.Status.STARTED) {
      let theseKeys = SpacePracticInst.getKeys({keyList: ['space'], waitRelease: false});
      _SpacePracticInst_allKeys = _SpacePracticInst_allKeys.concat(theseKeys);
      if (_SpacePracticInst_allKeys.length > 0) {
        SpacePracticInst.keys = _SpacePracticInst_allKeys[_SpacePracticInst_allKeys.length - 1].name;  // just the last key pressed
        SpacePracticInst.rt = _SpacePracticInst_allKeys[_SpacePracticInst_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PracticeInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeInstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'PracticeInstr'-------
    PracticeInstrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    // the Routine "PracticeInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyChimericPract_allKeys;
var PracticeTrialsComponents;
function PracticeTrialsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'PracticeTrials'-------
    t = 0;
    PracticeTrialsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    imageCenterPract.setPos([0, 0]);
    imageCenterPract.setImage(Image);
    imageLVFPract.setPos([(- 0.45), 0]);
    imageLVFPract.setImage(LVF);
    imageRVFPract.setPos([0.45, 0]);
    imageRVFPract.setImage(RVF);
    keyChimericPract.keys = undefined;
    keyChimericPract.rt = undefined;
    _keyChimericPract_allKeys = [];
    imageCentLabel.setText('الهدف');
    // keep track of which components have finished
    PracticeTrialsComponents = [];
    PracticeTrialsComponents.push(imageCenterPract);
    PracticeTrialsComponents.push(imageLVFPract);
    PracticeTrialsComponents.push(imageRVFPract);
    PracticeTrialsComponents.push(keyChimericPract);
    PracticeTrialsComponents.push(imageCentLabel);
    PracticeTrialsComponents.push(imageLVFLabel);
    PracticeTrialsComponents.push(imageRVFLabel);
    
    PracticeTrialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function PracticeTrialsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'PracticeTrials'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PracticeTrialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imageCenterPract* updates
    if (t >= 0.0 && imageCenterPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageCenterPract.tStart = t;  // (not accounting for frame time here)
      imageCenterPract.frameNStart = frameN;  // exact frame index
      
      imageCenterPract.setAutoDraw(true);
    }

    
    // *imageLVFPract* updates
    if (t >= 0.0 && imageLVFPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageLVFPract.tStart = t;  // (not accounting for frame time here)
      imageLVFPract.frameNStart = frameN;  // exact frame index
      
      imageLVFPract.setAutoDraw(true);
    }

    
    // *imageRVFPract* updates
    if (t >= 0.0 && imageRVFPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageRVFPract.tStart = t;  // (not accounting for frame time here)
      imageRVFPract.frameNStart = frameN;  // exact frame index
      
      imageRVFPract.setAutoDraw(true);
    }

    
    // *keyChimericPract* updates
    if (t >= 0.0 && keyChimericPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyChimericPract.tStart = t;  // (not accounting for frame time here)
      keyChimericPract.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyChimericPract.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyChimericPract.start(); }); // start on screen flip
    }

    if (keyChimericPract.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyChimericPract.getKeys({keyList: ['left', 'right', 'escape'], waitRelease: false});
      _keyChimericPract_allKeys = _keyChimericPract_allKeys.concat(theseKeys);
      if (_keyChimericPract_allKeys.length > 0) {
        keyChimericPract.keys = _keyChimericPract_allKeys[_keyChimericPract_allKeys.length - 1].name;  // just the last key pressed
        keyChimericPract.rt = _keyChimericPract_allKeys[_keyChimericPract_allKeys.length - 1].rt;
        // was this correct?
        if (keyChimericPract.keys == correct) {
            keyChimericPract.corr = 1;
        } else {
            keyChimericPract.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *imageCentLabel* updates
    if (t >= 0.0 && imageCentLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageCentLabel.tStart = t;  // (not accounting for frame time here)
      imageCentLabel.frameNStart = frameN;  // exact frame index
      
      imageCentLabel.setAutoDraw(true);
    }

    
    // *imageLVFLabel* updates
    if (t >= 0.0 && imageLVFLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageLVFLabel.tStart = t;  // (not accounting for frame time here)
      imageLVFLabel.frameNStart = frameN;  // exact frame index
      
      imageLVFLabel.setAutoDraw(true);
    }

    
    // *imageRVFLabel* updates
    if (t >= 0.0 && imageRVFLabel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageRVFLabel.tStart = t;  // (not accounting for frame time here)
      imageRVFLabel.frameNStart = frameN;  // exact frame index
      
      imageRVFLabel.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PracticeTrialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeTrialsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'PracticeTrials'-------
    PracticeTrialsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (keyChimericPract.keys === undefined) {
      if (['None','none',undefined].includes(correct)) {
         keyChimericPract.corr = 1;  // correct non-response
      } else {
         keyChimericPract.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('keyChimericPract.keys', keyChimericPract.keys);
    psychoJS.experiment.addData('keyChimericPract.corr', keyChimericPract.corr);
    if (typeof keyChimericPract.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyChimericPract.rt', keyChimericPract.rt);
        routineTimer.reset();
        }
    
    keyChimericPract.stop();
    // the Routine "PracticeTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keySpaceTrialsInstr_allKeys;
var TrialsInstrComponents;
function TrialsInstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'TrialsInstr'-------
    t = 0;
    TrialsInstrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keySpaceTrialsInstr.keys = undefined;
    keySpaceTrialsInstr.rt = undefined;
    _keySpaceTrialsInstr_allKeys = [];
    // keep track of which components have finished
    TrialsInstrComponents = [];
    TrialsInstrComponents.push(trialsInstr1);
    TrialsInstrComponents.push(trialsInstr2);
    TrialsInstrComponents.push(trialsInstr3);
    TrialsInstrComponents.push(trialsInstr4);
    TrialsInstrComponents.push(trialsInstr5);
    TrialsInstrComponents.push(textSpaceTrials);
    TrialsInstrComponents.push(keySpaceTrialsInstr);
    
    TrialsInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function TrialsInstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'TrialsInstr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = TrialsInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trialsInstr1* updates
    if (t >= 0.0 && trialsInstr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialsInstr1.tStart = t;  // (not accounting for frame time here)
      trialsInstr1.frameNStart = frameN;  // exact frame index
      
      trialsInstr1.setAutoDraw(true);
    }

    
    // *trialsInstr2* updates
    if (t >= 0.0 && trialsInstr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialsInstr2.tStart = t;  // (not accounting for frame time here)
      trialsInstr2.frameNStart = frameN;  // exact frame index
      
      trialsInstr2.setAutoDraw(true);
    }

    
    // *trialsInstr3* updates
    if (t >= 0.0 && trialsInstr3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialsInstr3.tStart = t;  // (not accounting for frame time here)
      trialsInstr3.frameNStart = frameN;  // exact frame index
      
      trialsInstr3.setAutoDraw(true);
    }

    
    // *trialsInstr4* updates
    if (t >= 0.0 && trialsInstr4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialsInstr4.tStart = t;  // (not accounting for frame time here)
      trialsInstr4.frameNStart = frameN;  // exact frame index
      
      trialsInstr4.setAutoDraw(true);
    }

    
    // *trialsInstr5* updates
    if (t >= 0.0 && trialsInstr5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialsInstr5.tStart = t;  // (not accounting for frame time here)
      trialsInstr5.frameNStart = frameN;  // exact frame index
      
      trialsInstr5.setAutoDraw(true);
    }

    
    // *textSpaceTrials* updates
    if (t >= 0.0 && textSpaceTrials.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpaceTrials.tStart = t;  // (not accounting for frame time here)
      textSpaceTrials.frameNStart = frameN;  // exact frame index
      
      textSpaceTrials.setAutoDraw(true);
    }

    
    // *keySpaceTrialsInstr* updates
    if (t >= 0.0 && keySpaceTrialsInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keySpaceTrialsInstr.tStart = t;  // (not accounting for frame time here)
      keySpaceTrialsInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keySpaceTrialsInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keySpaceTrialsInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keySpaceTrialsInstr.clearEvents(); });
    }

    if (keySpaceTrialsInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = keySpaceTrialsInstr.getKeys({keyList: ['space'], waitRelease: false});
      _keySpaceTrialsInstr_allKeys = _keySpaceTrialsInstr_allKeys.concat(theseKeys);
      if (_keySpaceTrialsInstr_allKeys.length > 0) {
        keySpaceTrialsInstr.keys = _keySpaceTrialsInstr_allKeys[_keySpaceTrialsInstr_allKeys.length - 1].name;  // just the last key pressed
        keySpaceTrialsInstr.rt = _keySpaceTrialsInstr_allKeys[_keySpaceTrialsInstr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TrialsInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialsInstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'TrialsInstr'-------
    TrialsInstrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "TrialsInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyChimeric_allKeys;
var ChimericTrialsComponents;
function ChimericTrialsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ChimericTrials'-------
    t = 0;
    ChimericTrialsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    imageCenter.setPos([0, 0]);
    imageCenter.setImage(Image);
    imageLVF.setPos([(- 0.45), 0]);
    imageLVF.setImage(LVF);
    imageRVF.setPos([0.45, 0]);
    imageRVF.setImage(RVF);
    keyChimeric.keys = undefined;
    keyChimeric.rt = undefined;
    _keyChimeric_allKeys = [];
    // keep track of which components have finished
    ChimericTrialsComponents = [];
    ChimericTrialsComponents.push(imageCenter);
    ChimericTrialsComponents.push(imageLVF);
    ChimericTrialsComponents.push(imageRVF);
    ChimericTrialsComponents.push(keyChimeric);
    
    ChimericTrialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function ChimericTrialsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ChimericTrials'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ChimericTrialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imageCenter* updates
    if (t >= 0.0 && imageCenter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageCenter.tStart = t;  // (not accounting for frame time here)
      imageCenter.frameNStart = frameN;  // exact frame index
      
      imageCenter.setAutoDraw(true);
    }

    
    // *imageLVF* updates
    if (t >= 0.0 && imageLVF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageLVF.tStart = t;  // (not accounting for frame time here)
      imageLVF.frameNStart = frameN;  // exact frame index
      
      imageLVF.setAutoDraw(true);
    }

    
    // *imageRVF* updates
    if (t >= 0.0 && imageRVF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageRVF.tStart = t;  // (not accounting for frame time here)
      imageRVF.frameNStart = frameN;  // exact frame index
      
      imageRVF.setAutoDraw(true);
    }

    
    // *keyChimeric* updates
    if (t >= 0.0 && keyChimeric.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyChimeric.tStart = t;  // (not accounting for frame time here)
      keyChimeric.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyChimeric.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyChimeric.start(); }); // start on screen flip
    }

    if (keyChimeric.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyChimeric.getKeys({keyList: ['left', 'right', 'escape'], waitRelease: false});
      _keyChimeric_allKeys = _keyChimeric_allKeys.concat(theseKeys);
      if (_keyChimeric_allKeys.length > 0) {
        keyChimeric.keys = _keyChimeric_allKeys[_keyChimeric_allKeys.length - 1].name;  // just the last key pressed
        keyChimeric.rt = _keyChimeric_allKeys[_keyChimeric_allKeys.length - 1].rt;
        // was this correct?
        if (keyChimeric.keys == correct) {
            keyChimeric.corr = 1;
        } else {
            keyChimeric.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ChimericTrialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ChimericTrialsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ChimericTrials'-------
    ChimericTrialsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (keyChimeric.keys === undefined) {
      if (['None','none',undefined].includes(correct)) {
         keyChimeric.corr = 1;  // correct non-response
      } else {
         keyChimeric.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('keyChimeric.keys', keyChimeric.keys);
    psychoJS.experiment.addData('keyChimeric.corr', keyChimeric.corr);
    if (typeof keyChimeric.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyChimeric.rt', keyChimeric.rt);
        routineTimer.reset();
        }
    
    keyChimeric.stop();
    // the Routine "ChimericTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyEnd_allKeys;
var EndScreenComponents;
function EndScreenRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'EndScreen'-------
    t = 0;
    EndScreenClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyEnd.keys = undefined;
    keyEnd.rt = undefined;
    _keyEnd_allKeys = [];
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(End);
    EndScreenComponents.push(keyEnd);
    
    EndScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function EndScreenRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'EndScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *End* updates
    if (t >= 0.0 && End.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      End.tStart = t;  // (not accounting for frame time here)
      End.frameNStart = frameN;  // exact frame index
      
      End.setAutoDraw(true);
    }

    
    // *keyEnd* updates
    if (t >= 0.0 && keyEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyEnd.tStart = t;  // (not accounting for frame time here)
      keyEnd.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyEnd.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyEnd.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyEnd.clearEvents(); });
    }

    if (keyEnd.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyEnd.getKeys({keyList: ['escape'], waitRelease: false});
      _keyEnd_allKeys = _keyEnd_allKeys.concat(theseKeys);
      if (_keyEnd_allKeys.length > 0) {
        keyEnd.keys = _keyEnd_allKeys[_keyEnd_allKeys.length - 1].name;  // just the last key pressed
        keyEnd.rt = _keyEnd_allKeys[_keyEnd_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'EndScreen'-------
    EndScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
