function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


function voteUp(id) {
    var vote_up = document.getElementById('button-up');
    var vote_down = document.getElementById('button-down');
    var counter = document.getElementById("counter");
    var xhr = new XMLHttpRequest();
    if (vote_up.getAttribute('data-state') === 'inactive') {
        xhr.open('POST', '/questions/vote/'+id+"/p/");
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        xhr.send();
        vote_up.style.color = '#00ff00';
        vote_down.style.color = '#555555';
        vote_up.setAttribute('data-state', 'active');
        vote_down.setAttribute('data-state', 'inactive');
        counter.innerHTML = parseInt(counter.innerHTML, 10)+1;
    } else {
        xhr.open('POST', '/questions/vote/'+id+"/m/");
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        xhr.send();
        vote_up.style.color = '#555555';
        vote_up.setAttribute('data-state', 'inactive');
        counter.innerHTML = parseInt(counter.innerHTML, 10)-1;
    }
}

function voteDown(id) {
    var vote_up = document.getElementById('button-up');
    var vote_down = document.getElementById('button-down');
    var xhr = new XMLHttpRequest();
    if (vote_down.getAttribute('data-state') === 'inactive') {
        xhr.open('POST', '/questions/vote/'+id+"/m/");
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        xhr.send();
        vote_down.style.color = '#00ff00';
        vote_up.style.color = '#555555';
        vote_down.setAttribute('data-state', 'active');
        vote_up.setAttribute('data-state', 'inactive');
        counter.innerHTML = parseInt(counter.innerHTML, 10)-1;
    } else {
        xhr.open('POST', '/questions/vote/'+id+"/p/");
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        xhr.send();
        vote_down.style.color = '#555555';
        vote_down.setAttribute('data-state', 'inactive');
        counter.innerHTML = parseInt(counter.innerHTML, 10)+1;
    }
}

