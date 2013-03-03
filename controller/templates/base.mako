<style>
div.block{
    border: 1px solid black;
    display: inline-block;
    margin: 2px;
    padding: 3px;
    width: 230px;
    border-radius: 5px;
    background-color: white;
}
div.block .name, div.block .picture, div.block .input{
  display: inline-block;
  vertical-align: middle;
}
div.block .name{
  height: 50px;
}
div.block .input, div.block .picture{
  float:right;
}
div.block.alive{
    background-color: white;
}
div.block.fallen{
    background-color: red;
}
</style>

<div style="width: 70%; margin-left: 15%; margin-right: 15%;">
    ${ next.body() }
</div>
