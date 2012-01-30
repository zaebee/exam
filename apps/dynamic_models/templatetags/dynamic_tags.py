from django import template
from dynamic_models.models import BaseDynamicModel

register = template.Library()
baseDynamic = BaseDynamicModel()


@register.inclusion_tag('dynamic_models/tags/dummy.html', takes_context=True)
def dynamic_tabs(context, template='dynamic_models/tags/dynamic_tabs.html'):
    """Return model_name, model.verbose_name dict on dymanic models"""
    models = {}
    for model_name, model in baseDynamic.registry.items():
        models.update({model_name: model._meta.verbose_name})

    return {'template': template,
            'models': models,
            }


class VerbatimNode(template.Node):

    def __init__(self, text):
        self.text = text

    def render(self, context):
        return self.text


@register.tag
def verbatim(parser, token):
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endverbatim':
            break
        if token.token_type == template.TOKEN_VAR:
            text.append('{{')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('{%')
        text.append(token.contents)
        if token.token_type == template.TOKEN_VAR:
            text.append('}}')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('%}')
    return VerbatimNode(''.join(text))
