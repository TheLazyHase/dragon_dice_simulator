<%inherit file='base.mako' />


<div style="border: 1px solid">
    Roll:
    % for result in results:
        <div>${result}</div>
    % endfor
</div>
<div style="border: 1px solid">
    Effects:
    % for event in events:
        <div>${event}</div>
    % endfor
</div>
<div style="border: 1px solid">
    Result:
    Melee: ${melee}<br />
    Missile: ${missile}<br />
    Save: ${save}<br />
</div>
<form method="get" action="/army/selection">
    <input type="submit" value="Return to selection" />
</form>
<form method="get" action="/army/${army_id}/edition">
    <input type="submit" value="Edit the army" />
</form>
<form method="get" action="/army/${army_id}/roll/test">
    <input type="submit" value="Dragon Roll" />
</form>
