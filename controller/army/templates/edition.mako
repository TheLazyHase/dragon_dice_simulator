<%inherit file='base.mako' />

<style>
div.block{
  border: 1px solid black;
}
div.block .name, div.block .picture, div.block .input{
  display: inline-block;
  vertical-align: middle;
}
div.block .name{
  height: 40px;
}
div.block .input, div.block .picture{
  float:right;
}
</style>

<div style="border: 1px solid;">
    <form method="POST" action="/army/edition/${army_id}">
        <div style="border: 1px solid; width: 180px; display: inline-block">
                <div style="border: 1px solid black; margin: auto; text-align: center;">
                    Available units
                </div>
                % for template in templates:
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
        <div style="border: 1px solid;">
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
        </div>
        <input type="submit" value="Save !" />
    </form>
</div>
