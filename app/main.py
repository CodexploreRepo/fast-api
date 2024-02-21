from random import randrange
from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

#extend from BaseModel of pydantic
class Post(BaseModel): 
    title: str
    content: str
    published: bool = True #default value if user not specified
    rating: Optional[int] = None #optinal field, int, with default value = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite food", "content": "I like piazze", "id": 2}
            ]
def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
# request Get methor url: "/"
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

 #need to update status_code = 201 if success
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post): #post will follow Post model
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}") #{id} : route_param, in str type
def get_post(id: int): #convert id to int
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} was not found")

    return {"post_detail" : post}


@app.delete("/posts/{id}")
def delete_post(id: int):
    #deleting post
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist")
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data': post_dict}    return {'data': post_dict}