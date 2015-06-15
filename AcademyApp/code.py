<caption><h2>Reviews</h2></caption>
    <ul>
    {% for review in restaurant.restaurantreview_set.all %}
        <li>
            <p>{{ review.rating }} star{{ review.rating|pluralize }}</p>
            <p>{{ review.comment }}</p>
            <p>Created by {{ review.user }} on {{ review.date }}</p>
        </li>
    {%	endfor	%}
    </ul>

    <caption><h3>Add review</h3></caption>
    <form action="{% url 'teacher_review_create' restaurant.id %}" method="post">
        {%	csrf_token	%}
        Message: <textarea name="comment" id="comment" rows="4"></textarea>
        <p>Rating:</p>
        <p>{% for rate in RATING_CHOICES %}
        <input type="radio"	name="rating" id="rating{{ forloop.counter }}" value="{{ rate.1 }}"	/>
        <label for="choice{{ forloop.counter }}">{{ rate.1 }} star{{ rate.0|pluralize }}</label>
        <br/>{%	endfor	%}
        </p>
        <input	type="submit"	value="Review"	/>
    </form>