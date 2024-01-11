const authForm = document.getElementById('enter-form');
const regForm = document.getElementById('reg-form')

document.querySelector('#authBtn').addEventListener('click',function(){
  authForm.classList.remove('hidden');
});

document.querySelector('#reg-btn_main').addEventListener('click',function(){
  regForm.classList.remove('hidden');
})

document.querySelector('#reg-btn_form').addEventListener('click',function(){
  regForm.classList.add('hidden');
})