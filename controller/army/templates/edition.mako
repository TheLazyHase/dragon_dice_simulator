<%inherit file='base.mako' />

<style>
div.block{
    border: 1px solid black;
    display: inline-block;
    margin-left: 5px;
    margin-right: 5px;
    width: 220px;
}
div.block .name, div.block .picture, div.block .input{
  display: inline-block;
  vertical-align: middle;
}
div.block{
  width: 220px;
}
div.block .name{
  height: 50px;
}
div.block .input, div.block .picture{
  float:right;
}
</style>

<script type="text/javascript">
    function toggle_visibility(id) {
       var e = document.getElementById(id);
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
    }
</script>

<div>
    <form method="POST" action="/army/edition/${army_id}">
        <div style="border: 1px solid; width: 70%; margin-left: 15%; margin-right: 15%;">
            <div style="border: 1px solid; width: 225px; display: inline-block; float: left">
                <div style="border: 1px solid black; margin: auto; text-align: center;">
                    Available units
                </div>
                % for race_name, race_tag, race_templates in races:
                <div style="border: 1px solid black; margin: auto; text-align: center;" onclick="toggle_visibility('container_${race_tag}')">
                    ${race_name}
                </div>
                    <div id="container_${race_tag}" style="display: none">
                    % for template in race_templates:
                        <% 
                            id = template['id'] 
                            name = template['name']
                            picture = template['picture']
                        %>
                        <div class="block">
                            <div class="name">${name}</div>
                            <div class="input"><input type="text" name="unit_amount_${id}" size="1" value="0" /></div>
                            <img class="picture" src="http://www.sfr-inc.com/${picture}" />
                        </div>
                    % endfor
                    </div>
                % endfor
            </div>
            % for dice in dices:
            <% 
                id = dice['id'] 
                name = dice['name']
                picture = dice['picture']
            %>
            <div class="block">
                <div class="name">${name}</div>
                <div class="input"><input type="checkbox" name="unit_to_remove[]" value="${id}" /></div>
                <img class="picture" src="http://www.sfr-inc.com/${picture}" />
            </div>
            % endfor
            <input type="submit" value="Save the change" />
        </div>
    </form>
    <form methid="get" action="/army/${army_id}/roll/test">
        <input type="submit" value="Dragon Roll" />
    </form
</div>
