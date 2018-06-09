import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './shared/material';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    NoopAnimationsModule,
    MaterialModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
