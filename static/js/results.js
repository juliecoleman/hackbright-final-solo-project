"use strict";

// const disableFavoriteButton = (buttonFav) => {
//    buttonFav.setAttribute('disabled', true);
// };


// $('.add-favorite').on('submit', (evt) => {
//   evt.preventDefault();
//   console.log(evt.target)
//   console.log(evt.target.value)
//   console.dir(evt.target)
 // disableFavoriteButton(evt.target);

//   const formInputs = {
//     'crop_id': $('#crop_id-field').val(),
//   };
//   console.log(formInputs)

//   $.post('/create-favorite', formInputs, (res) => {
//     alert(res);
//   });
// });

function addFavorite (id) {
  const formInputs = {
    'crop_id': id,
  };
  console.log(formInputs)
  // e.stopPropagation()
  $.post('/create-favorite', formInputs, (res) => {
    alert(res);
  });
  // return false; 
}

function createAccount () {
    $('#create-account').show();
};