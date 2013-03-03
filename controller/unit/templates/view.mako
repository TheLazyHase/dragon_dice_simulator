<%inherit file='controller:templates/base.mako' />

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

<div style="border: 1px solid; width: 220px; display: inline-block; border-radius: 5px;">
        <div style="border: 1px solid black; margin: auto; text-align: center;">
            <p style="padding: 0px; margin: 0px;">
            ${name}
            </p>
            <p style="padding: 0px; margin: 0px; font-size: 0.7em">
                ${info}
            </p>
        </div>
        <div style="text-align:center;">
            <div style="margin: auto;">
                % for face in faces:
                <% 
                    face_name = face['name']
                    picture = face['picture']
                %>
                <img class="picture" src="http://www.sfr-inc.com/${picture}" alt="${face_name}" title="${face_name}" />
                % endfor
            </div>
        </div>
</div>
