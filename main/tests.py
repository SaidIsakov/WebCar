# from django.test import TestCase


# {% extends "base.html" %}

# {% block main %}
# <div class="card text-bg-primary mb-3" style="max-width: 18rem;">
#     <div class="card-header">Заголовок</div>
#     <div class="card-body">
#       <h5 class="card-title">Название основной карты</h5>
#       <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#     </div>
#   </div>
#   <div class="card text-bg-secondary mb-3" style="max-width: 18rem;">
#     <div class="card-header">Заголовок</div>
#     <div class="card-body">
#       <h5 class="card-title">Название дополнительной карты</h5>
#       <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#     </div>
#   </div>
#   <div class="card text-bg-success mb-3" style="max-width: 18rem;">
#     <div class="card-header">Заголовок</div>
#     <div class="card-body">
#       <h5 class="card-title">Название карты успеха</h5>
#       <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#     </div>
#   </div>
#   <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
#     <div class="card-header">Заголовок</div>
#     <div class="card-body">
#       <h5 class="card-title">Название карты опасности</h5>
#       <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#     </div>
#   </div>
#   <div class="card text-bg-warning mb-3" style="max-width: 18rem;">
#     <div class="card-header">Заголовок</div>
#     <div class="card-body">
#       <h5 class="card-title">Название карточки с предупреждением</h5>
#       <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#     </div>
#   </div>
#   <div class="card text-bg-info mb-3" style="max-width: 18rem;">
#     <div class="card-header">Заголовок</div>
#     <div class="card-body">
#       <h5 class="card-title">Название информационной карты</h5>
#       <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#     </div>
#   </div>
#   <div class="card text-bg-light mb-3" style="max-width: 18rem;">
#     <div class="card-header">Заголовок</div>
#     <div class="card-body">
#       <h5 class="card-title">Название облегченной карты</h5>
#       <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#     </div>
#   </div>
#   <div class="card text-bg-dark mb-3" style="max-width: 18rem;">
#     <div class="card-header">Заголовок</div>
#     <div class="card-body">
#       <h5 class="card-title">Название темной карты</h5>
#       <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#     </div>
#   </div>
# {% endblock main %}





#КАРТОЧКИ В 4 РЯДА
# {% extends "base.html" %}

# {% block main %}
# <div class="container">
#   <div class="row">
#     <!-- Первый ряд -->
#     <div class="col-md-6">
#       <div class="card text-bg-primary mb-3">
#         <div class="card-header">Заголовок</div>
#         <div class="card-body">
#           <h5 class="card-title">Название основной карты</h5>
#           <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#         </div>
#       </div>
#     </div>
#     <div class="col-md-6">
#       <div class="card text-bg-secondary mb-3">
#         <div class="card-header">Заголовок</div>
#         <div class="card-body">
#           <h5 class="card-title">Название дополнительной карты</h5>
#           <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#         </div>
#       </div>
#     </div>
#   </div>

#   <!-- Второй ряд -->
#   <div class="row">
#     <div class="col-md-6">
#       <div class="card text-bg-success mb-3">
#         <div class="card-header">Заголовок</div>
#         <div class="card-body">
#           <h5 class="card-title">Название карты успеха</h5>
#           <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#         </div>
#       </div>
#     </div>
#     <div class="col-md-6">
#       <div class="card text-bg-danger mb-3">
#         <div class="card-header">Заголовок</div>
#         <div class="card-body">
#           <h5 class="card-title">Название карты опасности</h5>
#           <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#         </div>
#       </div>
#     </div>
#   </div>

#   <!-- Третий ряд -->
#   <div class="row">
#     <div class="col-md-6">
#       <div class="card text-bg-warning mb-3">
#         <div class="card-header">Заголовок</div>
#         <div class="card-body">
#           <h5 class="card-title">Название карточки с предупреждением</h5>
#           <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#         </div>
#       </div>
#     </div>
#     <div class="col-md-6">
#       <div class="card text-bg-info mb-3">
#         <div class="card-header">Заголовок</div>
#         <div class="card-body">
#           <h5 class="card-title">Название информационной карты</h5>
#           <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#         </div>
#       </div>
#     </div>
#   </div>

#   <!-- Четвертый ряд -->
#   <div class="row">
#     <div class="col-md-6">
#       <div class="card text-bg-light mb-3">
#         <div class="card-header">Заголовок</div>
#         <div class="card-body">
#           <h5 class="card-title">Название облегченной карты</h5>
#           <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#         </div>
#       </div>
#     </div>
#     <div class="col-md-6">
#       <div class="card text-bg-dark mb-3">
#         <div class="card-header">Заголовок</div>
#         <div class="card-body">
#           <h5 class="card-title">Название темной карты</h5>
#           <p class="card-text">Несколько кратких примеров текста для создания заголовка карточки и составления основной части содержимого карточки.</p>
#         </div>
#       </div>
#     </div>
#   </div>
# </div>
# {% endblock main %}