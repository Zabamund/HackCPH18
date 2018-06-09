import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatGridListModule } from '@angular/material/grid-list';


@NgModule({
  imports: [
    CommonModule,
    MatGridListModule
  ],
  declarations: [],
  exports: [
    MatGridListModule
  ]
})
export class MaterialModule { }
