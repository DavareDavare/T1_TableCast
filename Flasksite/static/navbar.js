import { LitElement, html, css } from 'https://cdn.skypack.dev/lit';

class Navbar extends LitElement {
  static styles = css`
    .navbar-nav.ml-auto {
      margin-left: auto;
    }
    
    .navbar-brand {
      font-size: 24px;
      padding: 10px;
    }
    
    .navbar-collapse {
      font-size: 20px;
    }
    
    .nav-item {
      padding: 10px;
    }
    
    .nav-link {
      padding: 10px;
    }

    .sticky {
      position: fixed;
      top: 0;
      width: 100%;
    }

  `;

  toggleNavbar() {
    const navbar = this.shadowRoot.querySelector('.navbar-collapse');
    navbar.classList.toggle('show');
  }

  render() {
    return html`
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
      
      <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <a class="navbar-brand" href="#">HTL SAALFELDEN</a>
        <button class="navbar-toggler" type="button" @click="${this.toggleNavbar}">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link" href="settings">Einstellungen</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="logout">Logout</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="login.html">Login</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="register.html">Registrieren</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="reboot">Reboot Pi</a>
            </li>
          </ul>
        </div>
      </nav>
    `;
  }
}

customElements.define('my-navbar', Navbar);
