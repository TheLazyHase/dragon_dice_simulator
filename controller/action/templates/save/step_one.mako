<%inherit file='controller:templates/base.mako' />


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
<form method="get" action="${route_next_step}">
    <input type="submit" value="Next step" />
</form>

