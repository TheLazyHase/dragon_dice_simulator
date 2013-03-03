<%inherit file='controller:templates/base.mako' />

<script type="text/javascript">
    function toggle_visibility(id) {
       var e = document.getElementById(id);
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
    }
</script>

<form method="POST" action="/army/${army_id}/edition">
    <div style="border: 1px solid; min-height: 650px; border-radius: 15px; background-color: #555555;">
        <div style="border: 1px solid; width: 240px; display: inline-block; float: left; border-radius: 10px; background-color: #999999; margin: 5px;">
            <div style="border: 1px solid black; margin: auto; text-align: center; border-radius: 10px; background-color: #BBBBBB;">
                Available units
            </div>
            % for race_name, race_tag, race_color, race_templates in races:
            <div style="border: 1px solid black; margin: auto; text-align: center; border-radius: 5px; background-color: #${race_color};" onclick="toggle_visibility('container_${race_tag}')">
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
<form method="get" action="/army/${army_id}/roll/missile_save" style="display: inline-block;">
    <input type="submit" value="Missile Save Roll" />
</form>
<form method="POST" action="/action/save" style="display: inline-block;">
    <input type="hidden" name="chosen_army" value="${army_id}" />
    <input type="text" name="damage" value="10" />
    <input type="submit" value="Melee Save action" />
</form>
