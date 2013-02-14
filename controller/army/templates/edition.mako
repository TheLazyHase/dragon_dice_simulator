<%inherit file='base.mako' />

<style>
div.block{
    border: 1px solid black;
    display: inline-block;
    margin: 2px;
    padding: 3px;
    width: 220px;
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

<div style="width: 70%; margin-left: 15%; margin-right: 15%;">
    <form method="POST" action="/army/${army_id}/edition">
        <div style="border: 1px solid; min-height: 600px; border-radius: 15px; background-color: grey;">
            <div style="border: 1px solid; width: 230px; display: inline-block; float: left; border-radius: 10px; background-color: white; margin: 5px;">
                <div style="border: 1px solid black; margin: auto; text-align: center; border-radius: 10px;">
                    Available units
                </div>
                % for race_name, race_tag, race_templates in races:
                <div style="border: 1px solid black; margin: auto; text-align: center; border-radius: 5px;" onclick="toggle_visibility('container_${race_tag}')">
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
    <form method="get" action="/army/selection">
        <input type="submit" value="Return to selection" />
    </form>
    <form method="get" action="/army/${army_id}/roll/dragon" style="display: inline-block;">
        <input type="submit" value="Dragon Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/melee" style="display: inline-block;">
        <input type="submit" value="Melee Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/missile" style="display: inline-block;">
        <input type="submit" value="Missile Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/maneuver" style="display: inline-block;">
        <input type="submit" value="Maneuver Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/melee_save" style="display: inline-block;">
        <input type="submit" value="Melee Save Roll" />
    </form>
    <form method="get" action="/army/${army_id}/roll/missile_save" style="display: inline-block;">
        <input type="submit" value="Missile Save Roll" />
    </form>
</div>
