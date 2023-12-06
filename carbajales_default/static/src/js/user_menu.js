/** @odoo-module **/
import { registry } from "@web/core/registry";
import { preferencesItem } from "@web/webclient/user_menu/user_menu_items";
import { routeToUrl } from "@web/core/browser/router_service";
import { browser } from "@web/core/browser/browser";
const usersMenuRegistry = registry.category("user_menuitems");
function vangrowSupportItems(env) {
  /**const URL = $.param.querystring(window.location.href, 'debug=1');**/
  const URL = "https://soporte.vangrow.com.ar/ayuda";
  return {
      type: "item",
      id: "vangrow_support",
      description: env._t("Soporte Vangrow S.A.S."),
      href: URL,
      callback: () => {
          browser.open(URL, "_blank").focus();
      },
      sequence: 10,
  };
}
registry.category("user_menuitems").add("vangrow_support", vangrowSupportItems)