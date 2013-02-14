<%inherit file='base.mako' />

<div style="border: 1px solid">
    Army named '${ name }' succesfully created !
</div>
<form methid="get" action="/army/${army_id}/edition">
    <input type="submit" value="Go to edition" />
</form>
