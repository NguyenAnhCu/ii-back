const list_response = ["false_responce1","false_responce2","false_responce3","false_responce4","false_responce5","false_responce6","false_responce7","true_responce"]

const json = {
   "true_responce":{
      "status":"correct",
      "explication":"Sur une m\u00eame ligne, le nombre d\u2019objet est le m\u00eame dans chaque imageSur une m\u00eame colonne, les objets de chaque image sont \u00e0 la m\u00eame position"
   },
   "false_responce1":{
      "status":"incorrect",
      "explication":"Sur une m\u00eame ligne, le nombre d\u2019objet est le m\u00eame dans chaque imageSur une m\u00eame colonne, les objets de chaque image sont \u00e0 la m\u00eame position"
   },
   "false_responce2":{
      "status":"incorrect",
      "explication":"Sur une m\u00eame ligne, le nombre d\u2019objet est le m\u00eame dans chaque imageSur une m\u00eame colonne, les objets de chaque image sont \u00e0 la m\u00eame position"
   },
   "false_responce3":{
      "status":"incorrect",
      "explication":"Sur une m\u00eame ligne, le nombre d\u2019objet est le m\u00eame dans chaque image"
   },
   "false_responce4":{
      "status":"incorrect",
      "explication":"Sur une m\u00eame ligne, le nombre d\u2019objet est le m\u00eame dans chaque imageSur une m\u00eame colonne, les objets de chaque image sont \u00e0 la m\u00eame position"
   },
   "false_responce5":{
      "status":"incorrect",
      "explication":"Sur une m\u00eame ligne, le nombre d\u2019objet est le m\u00eame dans chaque imageSur une m\u00eame colonne, les objets de chaque image sont \u00e0 la m\u00eame position"
   },
   "false_responce6":{
      "status":"incorrect",
      "explication":"Sur une m\u00eame ligne, le nombre d\u2019objet est le m\u00eame dans chaque imageSur une m\u00eame colonne, les objets de chaque image sont \u00e0 la m\u00eame position"
   },
   "false_responce7":{
      "status":"incorrect",
      "explication":"Sur une m\u00eame ligne, le nombre d\u2019objet est le m\u00eame dans chaque image"
   }
}
console.log(json.true_responce)


const clickImage = (alt) => {
    switch (alt){
        case "true_responce.png":
            alert('Your answer is correct. ' + `${json.true_responce.explication}`)
            break;
         case "false_responce1.png":
            alert('Your answer is incorrect. ' + `${json.false_responce1.explication}`)
            break;
         case "false_responce2.png":
            alert('Your answer is incorrect. ' + `${json.false_responce2.explication}`)
            break;
         case "false_responce3.png":
            alert('Your answer is incorrect. ' + `${json.false_responce3.explication}`)
            break;
         case "false_responce4.png":
            alert('Your answer is incorrect. ' + `${json.false_responce4.explication}`)
            break;
         case "false_responce5.png":
            alert('Your answer is incorrect. ' + `${json.false_responce5.explication}`)
            break;
         case "false_responce6.png":
            alert('Your answer is incorrect. ' + `${json.false_responce6.explication}`)
            break;
         case "false_responce7.png":
            alert('Your answer is incorrect. ' + `${json.false_responce7.explication}`)
            break;
        default:
            alert('nothing')
    }
}
let explication = []
function loadExplcation (){
    $.getJSON('/Users/cuanh/PycharmProjects/ii-back/question/question_explication.json', function(json){
        console.log(json)
    }).error(function(){
            console.log('error: json not loaded');
        });
    }

// const startButton = document.getElementById('start-btn')
// const nextButton = document.getElementById('next-btn')
// const questionContainerElement = document.getElementById('question-container')
// const questionElement = document.getElementById('question')
// const answerButtonsElement = document.getElementById('answer-buttons')
//
// let shuffledQuestions, currentQuestionIndex
//
// startButton.addEventListener('click', startGame)
// nextButton.addEventListener('click', () => {
//   currentQuestionIndex++
//   setNextQuestion()
// })
//
// function startGame() {
//   startButton.classList.add('hide')
//   shuffledQuestions = questions.sort(() => Math.random() - .5)
//   currentQuestionIndex = 0
//   questionContainerElement.classList.remove('hide')
//   setNextQuestion()
// }
//
// function setNextQuestion() {
//   resetState()
//   showQuestion(shuffledQuestions[currentQuestionIndex])
// }
//
// function showQuestion(question) {
//   questionElement.innerText = question.question
//   question.answers.forEach(answer => {
//     const button = document.createElement('button')
//     button.innerText = answer.text
//     button.classList.add('btn')
//     if (answer.correct) {
//       button.dataset.correct = answer.correct
//     }
//     button.addEventListener('click', selectAnswer)
//     answerButtonsElement.appendChild(button)
//   })
// }
//
// function resetState() {
//   clearStatusClass(document.body)
//   nextButton.classList.add('hide')
//   while (answerButtonsElement.firstChild) {
//     answerButtonsElement.removeChild(answerButtonsElement.firstChild)
//   }
// }
//
// function selectAnswer(e) {
//   const selectedButton = e.target
//   const correct = selectedButton.dataset.correct
//   setStatusClass(document.body, correct)
//   Array.from(answerButtonsElement.children).forEach(button => {
//     setStatusClass(button, button.dataset.correct)
//   })
//   if (shuffledQuestions.length > currentQuestionIndex + 1) {
//     nextButton.classList.remove('hide')
//   } else {
//     startButton.innerText = 'Restart'
//     startButton.classList.remove('hide')
//   }
// }
//
// function setStatusClass(element, correct) {
//   clearStatusClass(element)
//   if (correct) {
//     element.classList.add('correct')
//   } else {
//     element.classList.add('wrong')
//   }
// }
//
// function clearStatusClass(element) {
//   element.classList.remove('correct')
//   element.classList.remove('wrong')
// }
