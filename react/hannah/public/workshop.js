const addButton = document.querySelector('#add-food')

addButton.addEventListener('click', create_food, false);

function create_food() {
  const $food = document.querySelector('#food')

  if (!$food.value) {
    return false
  }

  const $item = document.createElement('li')
  $item.textContent = $food.value;
  poopFactory.add(food);
  food.value = '';

  document.querySelector('#poop-factory').appendChild($item)
}

function createPoopFactory() {
  const foods = [];
  const minFood = 1;

  return {
    add: function(food) {
      return foods.push(food);
    },
    poop: function() {
      return foods.length > minFood;
    }
  }
}

const $cat = document.querySelector('.cat')
$cat.addEventListener('click', displayPoop, false);

const $poop = document.querySelector('.cat__poop__icon')
$poop.classList.remove('cat__poop__icon--animate')

setTimeout(function() {
  const $poop = document.querySelector('.cat__poop__icon')
  $poop.classList.add('cat__poop__icon--animate')
})

const poopFactory = createPoopFactory()
